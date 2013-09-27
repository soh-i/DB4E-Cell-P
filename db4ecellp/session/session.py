__program__ = 'session'
__version__ = '0.0.1'
__author__ = 'Soh Ishiguro <t10078si@sfc.keio.ac.jp>'
__copyright__ = ''
__license__ = ''

import sys
import os
import ConfigParser

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

import species2
import genbank_generator
import regulondb_generator


def generate_decs(mapper):
    gen = genbank_generator.GenbankDecGenerator(mapper.GENBANK_FILE)
    gen.generate(mapper.session)
    gen = regulondb_generator.RegulonDBPromoterDecGenerator(
        mapper.PROMOTER_FILE)
    gen.generate(mapper.session)
    gen = regulondb_generator.RegulonDBPromoterDecGenerator(
        mapper.TERMINATOR_FILE)
    gen.generate(mapper.session)

path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path)

class DataInitializer(object):

    def __init__(self, conf):
        self.conf_filename = conf
        if not os.path.isfile(self.conf_filename):
            raise RuntimeError, "Configuration file [%s] is not found" % (
                os.path.abspath(self.conf_filename))

        conf = ConfigParser.RawConfigParser()
        conf.read(self.conf_filename)
        APP_ROOT = conf.get('root', 'APP_ROOT')

        # Read input file
        self.GENBANK_FILE    = APP_ROOT + conf.get('input_data', 'genbank')
        self.PROMOTER_FILE   = APP_ROOT + conf.get('input_data', 'promoter')
        self.TERMINATOR_FILE = APP_ROOT + conf.get('input_data', 'terminator')
        self.GENOME_SEQUENCE = APP_ROOT + conf.get('input_data', 'sequence')

        # Read output file
        # self.CDS_OUT        = APP_ROOT + conf.get('output_data', 'cds')
        # self.rRNA_OUT       = APP_ROOT + conf.get('output_data', 'rrna')
        # self.tRNA_OUT       = APP_ROOT + conf.get('output_data', 'trna')
        # self.PROMOTER_OUT   = APP_ROOT + conf.get('output_data', 'promoter')
        # self.TERMINATOR_OUT = APP_ROOT + conf.get('output_data', 'terminator')

        # DB
        self.DB_PATH = APP_ROOT + conf.get('db', 'db_path')

    def is_valid_file(self, filename):
        if not os.path.isfile(filename):
            raise IOError, "%s (wrote in %s) is not found" % (
                filename, self.conf_filename)

    def cleanup_data(self, *filenames):
        for filename in filenames:
            if os.path.isfile(filename):
                os.remove(filename)

class Mapper(DataInitializer):

    def __init__(self, conf):
        DataInitializer.__init__(self, conf)

        if os.path.isfile(self.DB_PATH):
            self.reflection = True
            # print "DB[%s] is exist" % (self.DB_PATH)
        else:
            self.reflection = False
            # print "DB[%s] is NOT exist" % (self.DB_PATH)

        self.engine = create_engine('sqlite:///' + self.DB_PATH, echo=False)

        if not self.reflection:
            # print "Reflection is OFF"
            species2.Base.metadata.create_all(self.engine)
        elif self.reflection:
            # print "Reflection is ON"
            metadata = MetaData(bind=self.engine)
            metadata.reflect(bind=self.engine)

        maker = sessionmaker(bind=self.engine)
        self.session = maker()

    def __destroy_DB(self):
        self.session.delete()

    def generate(self):
        if not self.reflection:
            # print "Generating DB..."
            generate_decs(self)
        elif self.reflection:
            # print "Use database reflection..."
            pass

class QueryBuilder(Mapper):

    def __init__(self, conf):
        Mapper.__init__(self, conf)

        self.generate()

    def count_stored_records(self):
        return self.session.query(species2.CDSDec).filter(species2.CDSDec.start).count()

    def collect_cds_records(self):
        all_rec = []
        for row in self.session.query(species2.CDSDec).all():
            all_rec.append(row)
        return all_rec

    def collect_all_gene_name(self):
        names = []
        for record in self.session.query(species2.CDSDec).order_by(species2.CDSDec.name):
            names.append(record.name)
        return names

    def find_by_name(self, gene_name):
        for rec in self.session.query(species2.CDSDec).filter_by(name=gene_name):
            return rec

    def collect_annotations_filter_by_strand(self, strand):
        filt_recs = []
        if strand == 1 or strand == -1:
            for rec in self.session.query(species2.CDSDec).filter_by(strand=strand):
                filt_recs.append(rec)
            return filt_recs
        else:
            raise RuntimeError, "Invalid argument given [%d], must be -1 or 1" % (strand)

    def include_record_in_region(self, start, end):
        records = []
        for record in self.session.query(species2.CDSDec).filter(species2.CDSDec.start.between(start, end)):
            records.append(record)
        return records

    def include_gene_in_region(self, start, end):
        genes = []
        for gene in self.session.query(species2.CDSDec).filter(species2.CDSDec.start.between(start, end)):
            # genes.append(gene.name)
            genes.append(gene)
        return genes

    def include_seq_in_region(self, start, end):
        seq = []
        for s in self.session.query(species2.CDSDec).filter(species2.CDSDec.start.between(start, end)):
            seq.append(s.sequence)
        return seq
