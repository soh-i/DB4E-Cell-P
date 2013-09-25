__program__ = 'generators'
__version__ = '0.0.1'
__author__ = 'Soh Ishiguro <t10078si@sfc.keio.ac.jp>'
__copyright__ = ''
__license__ = ''

from Bio import SeqIO
import sys
import os
import re
import os.path
from os import remove
import ConfigParser

path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path)


class DataInitializer(object):
    
    def __init__(self, conf):
        self.conf_file = conf
        if not os.path.isfile(self.conf_file):
            raise RuntimeError, "Configuration file [%s] is not found" % (os.path.abspath(self.conf_file))

        conf = ConfigParser.RawConfigParser()
        conf.read(self.conf_file)
        APP_ROOT = conf.get('root', 'APP_ROOT')

        # Read input file
        self.GENBANK_FILE    = APP_ROOT + conf.get('input_data', 'genbank')
        self.PROMOTER_FILE   = APP_ROOT + conf.get('input_data', 'promoter')
        self.TERMINATOR_FILE = APP_ROOT + conf.get('input_data', 'terminator')
        self.GENOME_SEQUENCE = APP_ROOT + conf.get('input_data', 'sequence')
        
        # Read output file
        self.CDS_OUT        = APP_ROOT + conf.get('output_data', 'cds')
        self.rRNA_OUT       = APP_ROOT + conf.get('output_data', 'rrna')
        self.tRNA_OUT       = APP_ROOT + conf.get('output_data', 'trna')
        self.PROMOTER_OUT   = APP_ROOT + conf.get('output_data', 'promoter')
        self.TERMINATOR_OUT = APP_ROOT + conf.get('output_data', 'terminator')
    
        # DB
        self.DB_PATH = APP_ROOT + conf.get('db', 'db_path')
        
    def is_valid_file(self, file):
        if not os.path.isfile(file):
            raise IOError, "%s (wrote in %s) is not found" % (file, self.conf_file)
    
    def clean_up_data(self, *file):
        for f in file:
            if os.path.isfile(f):
                os.remove(f)


# class Genbank(DataInitializer):
#     
#     def __init__(self, conf):
#         DataInitializer.__init__(self, conf)
#         
#     def generate_genbank_file(self):
#         self.is_valid_file(self.GENBANK_FILE)
#         
#         # if exist previous generated files, just remove it
#         self.clean_up_data(
#             self.CDS_OUT,
#             self.rRNA_OUT,
#             self.tRNA_OUT,
#             self.PROMOTER_OUT,
#             self.TERMINATOR_OUT
#         )
#         
#         handle = open(self.GENBANK_FILE, 'r')
#         cds_f  = open(self.CDS_OUT, 'a')
#         rrna_f = open(self.rRNA_OUT, 'a')
#         trna_f = open(self.tRNA_OUT, 'a')
#         
#         for record in SeqIO.parse(handle, 'genbank'):
#             for feature in record.features:
#                 if feature.type == 'CDS':
#                     if not 'pseudo' in feature.qualifiers and 'gene' in feature.qualifiers:
#                         gene = feature.qualifiers['gene'][0]
#                         start = feature.location.start
#                         end = feature.location.end
#                         strand = int(feature.location.strand)
#                         seq = record.seq[start:end]
#                         feature = feature.type
#                     
#                         cds_f.write("%s\t%d\t%s\t%s\t%s\t%s\n" % (gene, strand, start, end, feature, seq))
#                         
#                 elif feature.type == 'rRNA':
#                     gene = feature.qualifiers['gene'][0]
#                     start = feature.location.start
#                     end = feature.location.end
#                     strand = int(feature.location.strand)
#                     seq = record.seq[start:end]
#                     feature = feature.type
#                     
#                     rrna_f.write("%s\t%d\t%s\t%s\t%s\t%s\n" % (gene, strand, start, end, feature, seq))
#                         
#                 elif feature.type == 'tRNA':
#                     gene = feature.qualifiers['gene'][0]
#                     start = feature.location.start
#                     end = feature.location.end
#                     strand = int(feature.location.strand)
#                     seq = record.seq[start:end]
#                     feature = feature.type
# 
#                     trna_f.write("%s\t%d\t%s\t%s\t%s\t%s\n" % (gene, strand, start, end, feature, seq))

class Operon(DataInitializer):
    def __init__(self):
        raise NotImplementedError
        #DataInitializer.__init__(self)

    def generate_operon_file(self):
        """
        This script generates the operon DB from OperonSet.txt,
        input data was collected from web resource of the RegulonDB.
    
        URL    : http://regulondb.ccg.unam.mx/menu/download/datasets/files/OperonSet.txt
        OUTPUT : promoter_name    start    end    strand    gene_name(s)
        """
    
        header = "%s\t%s\t%s\t%s\t%s" % ("promoter_id", "start", "end", "strand", "gene name(s)")
        print header

        file = 'data/OperonSet.txt'
        with open(file, 'r') as f:
            for line in f:
            
                if not line.startswith("#") and not line.isspace():
                    data = line[:-1].split("\t")
                    name = data[0]
                    start = int(data[1])
                    end  = int(data[2])
                    strand = data[3]
                    num_operon = int(data[4])
                    gene_name = data[5]
                    
                    if 'forward' in strand:
                        strand = int(1)
                    elif 'reverse' in strand:
                        strand = int(-1)
                
                    print "%s\t%d\t%d\t%d\t%s" %(name, start, end, strand, gene_name)


class GenePromoterInteraction(DataInitializer):
    def __init__(self):
        raise NotImplementedError
        #DataInitializer.__init__(self)

    def generate_gene_promoter_interaction_file(self):
        """
        This script is used for generating promoter information per gene

        DATA URL: http://regulondb.ccg.unam.mx/menu/download/datasets/files/OperonSet.txt
        OUTPUT  : gene_name    strand    operon_id
        """

        file = 'data/OperonSet.txt'

        integrated_data = {}
        with open(file, 'r') as f:
            for line in f:
        
                if not line.startswith("#") and not line.isspace():
                    data = line[:-1].split("\t")
            
                    operon_name = 'OPERON_' + data[0]
                    start       = int(data[1])
                    end         = int(data[2])
                    strand      = data[3]
                    num_operon  = int(data[4])
                    gene_names  = data[5]
            
                    if 'forward' in strand:
                        strand = int(1)
                    elif 'reverse' in strand:
                        strand = int(-1)
                
                    gene = gene_names.split(",")
                    for g in gene:
                        integrated_data.update({g : {'operon_id' : operon_name, 'strand' : strand}})


