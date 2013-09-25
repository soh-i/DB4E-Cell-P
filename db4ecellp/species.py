__program__ = 'session'
__version__ = '0.0.1'
__author__ = 'Soh Ishiguro <t10078si@sfc.keio.ac.jp>'
__copyright__ = ''
__license__ = ''


from sqlalchemy import *
from sqlalchemy.orm import mapper, sessionmaker

metadata = MetaData()
class Species(object):
    
    __tablename__ = 'species'
    
    def __init__(self, name, strand, start, end, feature, sequence):
        self.name = name
        self.strand = int(strand)
        self.start = int(start)
        self.end = int(end)
        self.feature = feature
        self.sequence = sequence

    def __repr__(self):
        return "<Species('%s','%s','%d','%d','%s','%s')>" % (
            self.name, self.strand, self.start, self.end, self.feature, self.sequence)

species_table = Table('species', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String, nullable=False),
                      Column('strand', Integer, nullable=False),
                      Column('start', Integer, nullable=False),
                      Column('end',  Integer, nullable=False),
                      Column('feature', String, nullable=False),
                      Column('sequence', String, nullable=False),
                      sqlite_autoincrement=True
)


class CDS(Species):
    def __init__(self, name, strand, start, end, feature, sequence):
        Species.__init__(self, name, strand, start, end, feature, sequence)

cds_table = Table('cds', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String, nullable=False),
                  Column('strand', Integer, nullable=False),
                  Column('start', Integer, nullable=False),
                  Column('end', Integer, nullable=False),
                  Column('feature', String, nullable=False),
                  Column('sequence', String, nullable=False),
                  sqlite_autoincrement=True
)


class tRNA(Species):
    def __init__(self, name, strand, start, end, feature, sequence):
        Species.__init__(self, name, strand, start, end, feature, sequence)

trna_table = Table('trna', metadata,
                   Column('id', Integer,primary_key=True),
                   Column('name', String, nullable=False),
                   Column('strand', Integer, nullable=False),
                   Column('start', Integer, nullable=False),
                   Column('end', Integer, nullable=False),
                   Column('feature', String, nullable=False),
                   Column('sequence', String, nullable=False),
                   sqlite_autoincrement=True
)


class rRNA(Species):
    def __init__(self, name, strand, start, end, feature, sequence):
        Species.__init__(self, name, strand, start, end, feature, sequence)

rrna_table = Table('rrna', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String, nullable=False),
                   Column('strand', Integer, nullable=False),
                   Column('start', Integer, nullable=False),
                   Column('end', Integer, nullable=False),
                   Column('feature', String, nullable=False),
                   Column('sequence', String, nullable=False),
                   sqlite_autoincrement=True
)

class Promoter(Species):
    def __init__(self, name, strand, start, end, feature, sequence):
        Species.__init__(self, name, strand, start, end, feature, sequence)

promoter_table = Table('promoter', metadata,
                       Column('id',  Integer, primary_key=True),
                       Column('name', String, nullable=False),
                       Column('strand', Integer, nullable=False),
                       Column('start', Integer, nullable=False),
                       Column('end', Integer, nullable=False),
                       Column('feature', String, nullable=False),
                       Column('sequence', String, nullable=False),
                       sqlite_autoincrement=True
)

class Terminator(Species):
    def __init__(self, name, strand, start, end, feature, sequence):
        Species.__init__(self, name, strand, start, end, feature, sequence)

terminator_table = Table('terminator', metadata,
                         Column('id', Integer, primary_key=True),
                         Column('name', String, nullable=False),
                         Column('strand', Integer, nullable=False),
                         Column('start', Integer, nullable=False),
                         Column('end', Integer, nullable=False),
                         Column('feature', String, nullable=False),
                         Column('sequence', String, nullable=False),
                         sqlite_autoincrement=True
)

mapper(Species, species_table)
mapper(CDS, cds_table)
mapper(tRNA, trna_table)
mapper(rRNA, rrna_table)
mapper(Promoter, promoter_table)
mapper(Terminator, terminator_table)
