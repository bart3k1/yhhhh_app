FROM python:3

ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./requirements.txt

RUN apt-get update && \
    apt install build-essential nginx -y && \
    pip install -r requirements.txt && \
    mkdir /app &&\
    rm -rf /var/lib/apt/lists/*


ARG USER_ID=1000
ARG GROUP_ID=1000

RUN groupadd -g ${GROUP_ID} noroot &&\
    useradd -l -u ${USER_ID} -g noroot  -r -s /bin/bash noroot

COPY nginx.conf /etc/nginx/conf.d/
COPY start.sh /start.sh
RUN chmod a+x /start.sh

COPY . /app
# WORKDIR /app

CMD ["bash", "/start.sh"]