
__program__ = 'genbank_generator'
__version__ = '0.0.1'
__author__ = 'Soh Ishiguro, <t10078si@sfc.kei.ac.jp>'

from Bio import SeqIO
import sys
import os.path
import os


class DataGenerator(object):
    def __init__(self):
        self.file = file

    def clean_up_data(self):
        if os.path.isfile(self.file):
            os.remove(self.file)

    def set_data_type(self, file):
        pass
    
    gbk = '../../data/NC_000913.gbk'
    #fna = '../../data/test.fa'
    #prom = '../../data/PromoterSet.txt'
    #termin = '../../data/TerminatorSet.txt'
    
    regulonDB_files = {
        "Genbank" : gbk,
        #"GenomeSequence" : fna,
        #"Promoter" : prom,
        #"TerminatorSet" : termin
    }
        
class Promoter(DataGenerator):
    def __init__(self):
        DataGenerator.__init__(self)

class rRNA(DataGenerator):
    def __init__(self):
        DataGenerator.__init__(self)

class tRNA(DataGenerator):
    def __init__(self):
        DataGenerator.__init__(self)

class Genbank(DataGenerator):
    def __init__(self):
        DataGenerator.__init__(self)

    def generate_genbank(self):
        gbk_file = self.regulonDB_files["Genbank"]
        return gbk_file
        
        handle = open(gbk_file, 'r')
        cds_f  = open('data/CDS_annotation.tbl', 'a')
        rrna_f = open('data/rRNA_annotation.tbl', 'a')
        trna_f = open('data/tRNA_annotation.tbl', 'a')

        

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
                    
                        cds_f.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (gene, strand, start, end, feature, seq))
                
                        
                    elif feature.type == 'rRNA':
                        gene = feature.qualifiers['gene'][0]
                        start = feature.location.start
                        end = feature.location.end
                        strand = int(feature.location.strand)
                        seq = record.seq[start:end]
                        feature = feature.type
                    
                        rrna_f.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (gene, strand, start, end, feature, seq))
                        
                    elif feature.type == 'tRNA':
                        gene = feature.qualifiers['gene'][0]
                        start = feature.location.start
                        end = feature.location.end
                        strand = int(feature.location.strand)
                        seq = record.seq[start:end]
                        feature = feature.type

                        trna_f.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (gene, strand, start, end, feature, seq))


gb = Genbank()
print gb.generate_genbank()

