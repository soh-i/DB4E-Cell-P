#!/usr/bin/env python 

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy.orm import sessionmaker

uri = 'sqlite:////Users/yukke/dev/DB4E-Cell-P/data/ecoli.db'
engine = create_engine(uri, echo=True)
Session = sessionmaker(bind=engine)
session = Session()



