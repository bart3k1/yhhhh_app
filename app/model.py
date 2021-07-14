from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String


Base=declarative_base()
DB_URI = 'postgresql+psycopg2://myuser:mypass@localhost/mydb'

class ToDoBase(Base):
    __tablename__='account'
    id = Column(Integer,primary_key=True)
    text = Column(String(100))
    status = Column(String(100))
    date_added = Column(String(50))
    # checked = Column(String(50))


if __name__ == "__main__":
 from sqlalchemy import create_engine
 engine = create_engine(DB_URI)
 Base.metadata.drop_all(engine)
 Base.metadata.create_all(engine)


