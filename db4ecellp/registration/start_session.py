
__author__ = 'Soh Ishiguro <t10078si@sfc.keio.ac.jp>'
__version__ = '0.0.1'

from species import species
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker


class Mapper(object):
    def __init__(self):
        self.engine = species.create_engine('sqlite:///:memory:', echo=False)
        species.metadata.create_all(self.engine)
        self.Session = species.sessionmaker()
        self.Session.configure(bind=self.engine)
        self.session = self.Session()

    def mapping_CDS(self):
        with open("../../data/CDS_annotation.tbl", "r") as f:
            for line in f:
                (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
                obj = species.CDS(name, strand, start, end, feature, sequence)
                self.session.add(obj)
        self.session.commit()

    def retrieve_all_records(self):
        all_rec = []
        for row in self.session.query(species.CDS).all():
            all_rec.append(row)
        return all_rec
            
    def query_by_all_cds(self):
        for record in self.session.query(species.CDS).order_by(species.CDS.name):
            return record.name

    def query_by_region(self, start, end):
        records = []
        for record in self.session.query(species.CDS).filter(species.CDS.start.between(start, end)):
            records.append(record)
        return records

    def query_by_region_with_gene(self, start, end):
        genes = []
        for gene in self.session.query(species.CDS).filter(species.CDS.start.between(start, end)):
            genes.append(gene.name)
        return genes
        
    def query_by_region_with_seq(self):
        seq = []
        for s in self.session.query(species.CDS).filter(species.CDS.start.between(start, end)):
            seq.append(s.sequence)
        return seq
        
    def query_by_region_with_strand(self):
        pass
    
    def query_by_gene_name(self, gene_name):
        for name in self.session.query(species.CDS).filter_by(name=gene_name):
            return name


if __name__ == '__main__':
    # create Mapper class object
    mapper = Mapper()
    
    # Map CDS table to db
    mapper.mapping_CDS()
    
    
    #print "Mapping CDS table to DB is finished"
    
    #print mapper.retrieve_all_records()
    #print mapper.query_by_all_cds()
    #print mapper.query_by_gene_name('thrL')
    #print mapper.query_by_region(189, 12255)
    print mapper.query_by_region_with_gene(189,3010)



    
