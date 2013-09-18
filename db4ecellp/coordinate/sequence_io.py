
__author__ = 'Soh Ishiguro <t10078si@sfc.keio.ac.jp>'
__version__ = '0.0.1'

import os.path
from Bio import SeqIO


class GenomicCoordinateException(Exception):
    
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "Genomic position is only 1-origin, given value of %d, %d were not accepted" % (self.start, self.end)

class SequenceIOException(Exception):
    
    def __init__(self, file):
        self.file = file
        
    def __str__(self):
        return ""


class SequenceIO(object):
    
    def __init__(self, file='', circular=True):
        # Error check
        if os.path.splitext(file)[1] != '.fasta':
            raise RuntimeError("Error: fasta format is only accepted")
        if not os.path.exists(file):
            raise RuntimeError("Error: given file is not found")
            
        self.seq = file
        self.circular = circular # default: circular genome
    
    def read_sequence(self):
        record = SeqIO.read(self.seq, "fasta")
        self.rec = []

        for i in record.seq:
            self.rec.append([i])
        return self.rec

    def is_valid_sequence(self):
        pass

    def sequence_file_name(self):
        return self.seq

    def print_sequence(self, all=False):
        limit = 5000
        concentrated_seq = ''
        
        if all:
            for s in self.rec:
                concentrated_seq += str(s[0])
            return concentrated_seq
            
        else:
            for index, seq in enumerate(self.rec):
                concentrated_seq += str(seq[0])
                if index > limit:
                    break
            return concentrated_seq
        

class GenomicCoordinate(SequenceIO):
    
    def __init__(self):
        SequenceIO.__init__(self)
        
    def is_circular(self):
        pass

    def seq_name(self):
        return self.fasta

    def get_sequence_region_from_genome(self):
        pass

    def map_sequence_region_to_genome(self):
        pass


class GenomicAttribute(object):
    
    def __init__(self, start='', end=''):
        self.start = start
        self.end = end

    def get_gene_seq(self):
        pass

    def get_gene_name(self):
        pass

    def get_gene_annotation_from_position(self):
        pass


    

