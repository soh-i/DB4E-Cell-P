
__author__ = 'Soh Ishiguro <t10078si@sfc.keio.ac.jp>'
__version__ = '0.0.1'

import string
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
    
    def insert_sequence(self, start, original_seq, insert_seq):
        pre = original_seq[0:start]
        post = original_seq[start:end]
        self.inesrt = pre + insert_seq + post
        return self.insert
        
    def sequence_file_name(self):
        return self.seq
    
    def fasta_header(self):
        record = SeqIO.read(self.seq, "fasta")
        return record.id

    def get_complement_seq(self):
        self.rev_seq = []
        record = SeqIO.read(self.seq, 'fasta')
        
        for nuc in record.seq:
            if nuc == 'A' or nuc == 'a':
                self.rev_seq.append(['T'])
            elif nuc == 'T' or nuc == 't':
                self.rev_seq.append(['A'])
            elif nuc == 'G' or nuc == 'g':
                self.rev_seq.append(['C'])
            elif nuc == 'C' or nuc == 'c':
                self.rev_seq.append(['G'])
            elif nuc == 'n' or nuc == 'N':
                self.rev_seq.append(['n'])
                
        return self.rev_seq
        
    def get_reverse_complement_seq(self):
        pass

    def print_sequence(self, all=False):
        limit = 100
        concentrated_seq = ''
        
        if all:
            for s in self.rec:
                concentrated_seq += str(s[0])
            return concentrated_seq
   
        elif not all:
            for index, seq in enumerate(self.rec):
                concentrated_seq += str(seq[0])
                if index > limit:
                    break
            return concentrated_seq
        

class GenomicCoordinate(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_circular(self):
        return self.start
    
    def seq_name(self):
        return self.fasta

    def get_sequence_region_from_circular(self):
        if self.start > self.end:
            return self.sequence[self.start-1:self.end]

        elif self.end < self.start:
            return self.sequence[self.start:self.length % self.end]
            
        elif self.start > 0 and self.end > 0:
            return self.sequence[self.start-1:self.end]

        elif self.start > 0 and self.end < 0:
            return self.sequence[self.start-1:self.length-abs(self.end)]

        elif self.start < 0 and self.end > 0:
            return self.sequence[self.start-1:self.length-abs(self.end)]
            
        elif self.start < 0 and self.end < 0:
            return self.sequence[self.length-abs(end):self.length-abs(self.start)]
        
    def get_sequence_region_from_linear(self):
        if self.start > 0 and self.end > 0:
            return self.sequence[self.start-1:self.end]

        elif self.start > 0 and self.end > self.length:
            return self.sequence[self.start-1:self.length]
            
        elif self.start > self.length:
            return ''

    def map_attribute_to_genome(self):
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

    def find_all_gene_names(self):
        pass

    def find_all_cds(self):
        pass

    def is_strand(self):
        pass

    def is_circular(self):
        pass

    def size_of_genome(self):
        pass

    def is_traslated(self):
        pass


