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


class DataInitializer(object):
    
    def __init__(self):
        __regulonDB_files = {
            'Genbank':'../data/NC_000913.gbk',
            'GenomeSequence':'../data/test.fa',
            'Promoter':'../data/PromoterSet.txt',
            'Terminator':'../data/TerminatorSet.txt',
            #'Operon':'../data/',
        }
        self.__regulonDB_files = __regulonDB_files
    
    def query_file_by_format(self, format):
        if os.path.isfile(self.__regulonDB_files[format]):
            return self.__regulonDB_files[format]
        else:
            raise IOError, "Given file(format=[%s, %s]) is not found." % (format, os.path.abspath(self.__regulonDB_files[format]))
    
    def clean_up_data(self, *file):
        for f in file:
            if os.path.isfile(f):
                os.remove(f)

    def add_additional_annotation(self, file_path, db_name):
        self.__regulonDB_files.update({db_name:file_path})


class Genbank(DataInitializer):
    
    def __init__(self):
        DataInitializer.__init__(self)
        
    def generate_genbank_file(self):
        # get Genbank file path
        gbk_file = self.query_file_by_format("Genbank")
        
        # output generated annotation files
        cds_file = '../data/CDS_annotation.tbl'
        trna_file = '../data/tRNA_annotation.tbl'
        rrna_file = '../data/rRNA_annotation.tbl'
        
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

    def generate_promoter_file(self):
        promoter_file = self.query_file_by_format("Promoter")
        
        output_file = open('../data/promoter_annotation.tbl','w');
        
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

    def generate_terminator_file(self):
        terminator_file = self.query_file_by_format("Terminator")
        output_file = open('../data/terminator_annotation.tbl','w');

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

        file = '/home/soh.i/E-cell_Sprint/RegulonDATADist/OperonSet.txt'
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

        file = '/home/soh.i/E-cell_Sprint/RegulonDATADist/OperonSet.txt'

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


