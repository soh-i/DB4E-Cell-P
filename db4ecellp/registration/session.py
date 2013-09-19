
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

    def __mapping_CDS(self):
        with open("../../data/CDS_annotation.tbl", "r") as f:
            for line in f:
                (name, strand, start, end, feature, sequence) = line[:-1].split("\t")
                obj = species.CDS(name, strand, start, end, feature, sequence)
                self.session.add(obj)
        self.session.commit()

    def __map_tRNA(self):
        pass

    def __map_rRNA(self):
        pass

    def __map_promoter(self):
        pass

    def __map_terminater(self):
        pass
    
    def generate_db(self):
        self.__mapping_CDS()


class Query(Mapper):

    def __init__(self):
        Mapper.__init__(self)
        self.generate_db()
        
    def count_stored_records(self):
        return self.session.query(species.CDS).filter(species.CDS.start).count()

    def collect_all_records(self):
        all_rec = []
        for row in self.session.query(species.CDS).all():
            all_rec.append(row)
        return all_rec

    def collect_gene_by_name(self, gene_name):
        for name in self.session.query(species.CDS).filter_by(name=gene_name):
            return name
    
    def collect_all_annotations_by_strand(self, strand):
        filt_recs = []
        if strand == 1 or strand == -1:
            for rec in self.session.query(species.CDS).filter_by(strand=strand):
                filt_recs.append(rec)
            return filt_recs
        else:
            raise ValueError
            
    def collec_all_gene_name(self):
        names = []
        for record in self.session.query(species.CDS).order_by(species.CDS.name):
            names.append(record.name)
        return names

    def include_record_in_region(self, start, end):
        records = []
        for record in self.session.query(species.CDS).filter(species.CDS.start.between(start, end)):
            records.append(record)
        return records

    def include_gene_in_region(self, start, end):
        genes = []
        for gene in self.session.query(species.CDS).filter(species.CDS.start.between(start, end)):
            genes.append(gene.name)
        return genes
        
    def include_seq_in_region(self, start, end):
        seq = []
        for s in self.session.query(species.CDS).filter(species.CDS.start.between(start, end)):
            seq.append(s.sequence)
        return seq

    
