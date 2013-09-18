
__author__ = 'Soh Ishiguro <t10078si@sfc.keio.ac.jp>'
__version__ = '0.0.1'


class GenomicCoordinateException(Exception):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "Genomic position is only 1-origin, given value of %d, %d were not accepted" % (self.start, self.end)


class SequenceIO(object):
    def __init__(self, fasta):
        self.fasta = fasta
    
    def is_valid_sequence(self):
        pass

    def generate_genomic_array(self):
        
        from Bio import SeqIO
        
        record = SeqIO.read(self.seq, "fasta")
        self.rec = []

        for i in record.seq:
            self.rec.append([i])
        return self.rec

    def write_sequence(self):
        pass


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
    def __init__(self):
        pass

    def get_gene_seq(self):
        pass

    def get_gene_name(self):
        pass

    def get_gene_annotation_from_position(self):
        pass


    

