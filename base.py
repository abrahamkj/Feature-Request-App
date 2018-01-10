# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:root@127.0.0.1:3306/test')
Session = sessionmaker(bind=engine)

Base = declarative_base()
