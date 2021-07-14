FROM python:3

ENV PYTHONUNBUFFERED=1

COPY /app/requirements.txt ./requirements.txt

RUN apt-get update && \
    apt install build-essential nginx -y && \
    pip install -r requirements.txt && \
    mkdir /app

ARG USER_ID=1000
ARG GROUP_ID=1000

RUN groupadd -g ${GROUP_ID} nginx &&\
    useradd -l -u ${USER_ID} -g nginx nginx &&\
    install -d -m 0755 -o nginx -g nginx /home/nginx

# Install Supervisord
RUN apt-get update && apt-get install -y supervisor \
&& rm -rf /var/lib/apt/lists/*
# Custom Supervisord config
COPY supervisord-debian.conf /etc/supervisor/conf.d/supervisord.conf

# RUN chmod g+wx /var/log/ 

#  Remove default configuration from Nginx
# RUN rm /etc/nginx/conf.d/default.conf
# Copy the base uWSGI ini file to enable default dynamic uwsgi process number
COPY /app/uwsgi.ini /etc/uwsgi/
COPY /app/uwsgi.ini /app/uwsgi.ini
# COPY /app/nginx.conf /app/app/nginx.conf

 
# Which uWSGI .ini file should be used, to make it customizable
ENV UWSGI_INI /app/uwsgi.ini

# By default, run 2 processes
# ENV UWSGI_CHEAPER 2

# By default, when on demand, run up to 16 processes
# ENV UWSGI_PROCESSES 16

# By default, allow unlimited file sizes, modify it to limit the file sizes
# To have a maximum of 1 MB (Nginx's default) change the line to:
# ENV NGINX_MAX_UPLOAD 1m
# ENV NGINX_MAX_UPLOAD 0

# By default, Nginx will run a single worker process, setting it to auto
# will create a worker for each CPU core
# ENV NGINX_WORKER_PROCESSES 1

# By default, Nginx listens on port 80.
# To modify this, change LISTEN_PORT environment variable.
# (in a Dockerfile or with an option for `docker run`)
# ENV LISTEN_PORT 80


COPY entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
COPY start.sh /start.sh
RUN chmod a+x /start.sh

COPY . /app
WORKDIR /app
EXPOSE 80

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Supervisor, which in turn will start Nginx and uWSGI
CMD ["/start.sh"]