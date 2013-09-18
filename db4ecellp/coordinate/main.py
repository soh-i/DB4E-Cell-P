#!/usr/bin/python 

from sequence_io import SequenceIO
from sequence_io import GenomicCoordinate
from sequence_io import GenomicAttribute

seq_file = '../../data/seq.fasta'
seq_io = SequenceIO(seq=seq_file, circular=True)
print seq_io.sequence_file_name()
genomic_array = seq_io.generate_genomic_array()


#print seq_io.seq_name()
#print seq_io.get_sequence_region_from_genome(start=1, end=200)
#print seq_io.get_gene_annotation_from_position(start=1, end=200)





