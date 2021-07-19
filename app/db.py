from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

db_engine = create_engine('postgresql+psycopg2://myuser:mypass@localhost:5432/mydb')

session_factory = sessionmaker(bind=db_engine)
Session = scoped_session(session_factory)


