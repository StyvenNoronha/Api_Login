#pip install pymysql
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

usuario =''
senha = ''
host = ''
banco = ''
port = ''

conn = f'mysql+pymysql://{usuario}:{senha}@{host}:{port}/{banco}'

engine = create_engine(conn, echo=True) # type: ignore
Session = sessionmaker(bind=engine) # type: ignore
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'Pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))

class Tokens(Base):
    __tablename__ = 'Tokens'
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey('Pessoa.id'))
    token = Column(String(100))    
    data = Column(DateTime, default=datetime.datetime.utcnow())


Base.metadata.create_all(engine)    # type: ignore