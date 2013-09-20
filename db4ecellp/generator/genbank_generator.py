__program__ = 'genbank_generator'
__version__ = '0.0.1'
__author__ = 'Soh Ishiguro <t10078si@sfc.keio.ac.jp>'
__copyright__ = ''
__license__ = ''

from Bio import SeqIO
import sys
import os.path
import os

from data_initializer import DataInitializer


class Genbank(DataInitializer):
    def __init__(self):
        DataInitializer.__init__(self)
        
    def generate_genbank_db(self):
        # get Genbank file path
        gbk_file = self.query_file_by_format("Genbank")
        cds_file = '../../data/CDS_annotation.tbl'
        trna_file = '../../data/tRNA_annotation.tbl'
        rrna_file = '../../data/rRNA_annotation.tbl'
        
        # if exist previous generated files, remove it
        self.clean_up_data(cds_file, rrna_file, trna_file)
        
        handle = open(gbk_file, 'r')
        cds_f  = open(cds_file, 'a')
        rrna_f = open(rrna_file, 'a')
        trna_f = open(trna_file, 'a')
        
        for record in SeqIO.parse(handle, 'genbank'):
            for feature in record.features:
                if feature.type == 'CDS':
                    if not 'pseudo' in feature.qualifiers and 'gene' in feature.qualifiers:
                        gene = feature.qualifiers['gene'][0]
                        start = feature.location.start
                        end = feature.location.end
                        strand = int(feature.location.strand)
                        seq = record.seq[start:end]
                        feature = feature.type
                    
                        cds_f.write("%s\t%d\t%s\t%s\t%s\t%s\n" % (gene, strand, start, end, feature, seq))
                
                        
                elif feature.type == 'rRNA':
                    gene = feature.qualifiers['gene'][0]
                    start = feature.location.start
                    end = feature.location.end
                    strand = int(feature.location.strand)
                    seq = record.seq[start:end]
                    feature = feature.type
                    
                    rrna_f.write("%s\t%d\t%s\t%s\t%s\t%s\n" % (gene, strand, start, end, feature, seq))
                        
                elif feature.type == 'tRNA':
                    gene = feature.qualifiers['gene'][0]
                    start = feature.location.start
                    end = feature.location.end
                    strand = int(feature.location.strand)
                    seq = record.seq[start:end]
                    feature = feature.type

                    trna_f.write("%s\t%d\t%s\t%s\t%s\t%s\n" % (gene, strand, start, end, feature, seq))

