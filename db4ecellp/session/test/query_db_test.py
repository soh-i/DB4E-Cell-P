from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

import sys
sys.path.append('../species')
from species import Species, CDS, tRNA, rRNA, Promoter, Terminator

engine = create_engine('sqlite:///test.db', echo=False)
metadata = MetaData(bind=engine)
metadata.reflect() # use reflection

Session = sessionmaker(bind=engine)
session = Session()

print session.query(CDS).filter_by(name="thrL").all()
