#!/usr/bin/env python

__author__ = 'Soh Ishiguro <t10078si@sfc.keio.ac.jp>'
__version__ = '0.0.1'

from species import species
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = species.create_engine('sqlite:///:memory:', echo=False)
species.metadata.create_all(engine)
Session = species.sessionmaker()
Session.configure(bind=engine)
session = Session()

with open("../../data/CDS_annotation.tbl", "r") as f:
    for line in f:
        (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
        obj = species.CDS(name, strand, start, end, feature, sequence)
        session.add(obj)

session.commit()



"""
def generate_db():
    
    engine = species.create_engine('sqlite:///:memory', echo=False)
    species.metadata.create_all(engine)
    Session = species.sessionmaker()
    
    Session.configure(bind=engine)
    session = Session()

    with open("data/CDS_annotation.tbl", "r") as f:
        for line in f:
            (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
            obj = species.CDS(name, strand, start, end, feature, sequence)
            session.add(obj)

    with open("data/rRNA_annotation.tbl", "r") as f:
        for line in f:
            (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
            obj = species.rRNA(name, strand, start, end, feature, sequence)
            session.add(obj)

    with open("data/tRNA_annotation.tbl", "r") as f:
        for line in f:
            (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
            obj = species.tRNA(name, strand, start, end, feature, sequence)
            session.add(obj)

    with open("data/promoter_annotation.tbl", "r") as f:
        for line in f:
            (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
            obj = species.Promoter(name, strand, start, end, feature, sequence)
            session.add(obj)

    with open("data/terminator_annotation.tbl", "r") as f:
        for line in f:
            (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
            obj = species.Terminator(name, strand, start, end, feature, sequence)
            session.add(obj)
            
    session.commit()

"""
