__program__ = 'data_initializer'
__version__ = '0.0.1'
__author__ = 'Soh Ishiguro <t10078si@sfc.keio.ac.jp>'
__copyright__ = ''
__license__ = ''

from Bio import SeqIO
import os.path
from os import remove


class DataInitializer(object):
    '''
    Base class for the generating DB from some annotation resources(e.g.: regSeq, RegulonDB).
    '''
    
    def __init__(self):
        # register row db files
        __regulonDB_files = {
            'Genbank':'../../data/NC_000913.gbk',
            'GenomeSequence':'',
            'Promoter':'',
            'TerminatorSet':'',
        }
        self.__regulonDB_files = __regulonDB_files
    
    def query_file_by_format(self, format):
        if os.path.isfile(self.__regulonDB_files[format]):
            return self.__regulonDB_files[format]
        else:
            raise IOError, "Given file(format=[%s]) is not found." % (format)
    
    def clean_up_data(self, *file):
        for f in file:
            if os.path.isfile(f):
                os.remove(f)

    def add_additional_annotation(self, file_path, db_name):
        self.__regulonDB_files.update({db_name:file_path})

