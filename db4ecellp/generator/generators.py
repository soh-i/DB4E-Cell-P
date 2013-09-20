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


class Promoter(DataInitializer):
    def __init__(self):
        DataInitializer.__init__(self)

    def generate_annotation_files():
        promoter_file = self.query_file_by_format("Promoter")
        
        output_file = open('../../data/promoter_annotation.tbl','w');
        
        for line in open(promoter_file, 'r'):
            if (line.isspace()):
                continue

            line = line.rstrip()
            if not re.match('^#',line):
                lineArray = line.split("\t")
            
                if not len(lineArray) == 7 :
                    continue

                if lineArray[2] in "forward":
                    text = "\t".join([ lineArray[0],"1",lineArray[3],lineArray[3],"promoter",lineArray[5] ])
                    output_file.write(text + "\n")
                else:
                    text = "\t".join([ lineArray[0],"-1",lineArray[3],lineArray[3],"promoter",lineArray[5] ])
                    output_file.write(text + "\n")


class Terminator(DataInitializer):
    '''
    Name: Satoshi Tamaki
    E-mail: coela.st@gmail.com

    This script generates the operon DB from TerminatorSet.txt,
    input data was collected from web resource of the RegulonDB.(not from Web page)
    http://regulondb.ccg.unam.mx/menu/download/datasets/files/TerminatorSet.txt

    OUTPUT : terminator_id strand start end type(terminator) sequence
    Terminator information from
    '''

    def __init__(self):
        DataInitializer.__init__(self)

    def generate_annotation_files():
        terminator_file = self.query_file_by_format("Terminator")
    
        output_file = open('data/terminator_annotation.tbl','w');

        for line in open(terminator_file, 'r'):
            line = line.rstrip()
            if not re.match('^[#]',line) and re.match('^\S',line):
                lineArray = line.split("\t")
                if lineArray[3] in "forward":
                    text = "\t".join([lineArray[0],"1",lineArray[1],lineArray[2],"terminator",lineArray[4] ])
                    output_file.write(text + "\n")
                else:
                    text = "\t".join([lineArray[0],"-1",lineArray[1],lineArray[2],"terminator",lineArray[4] ])
                    output_file.write(text + "\n")

