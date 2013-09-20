__program__ = 'annotation_builder'
__version__ = '0.0.1'
__author__ = 'Soh Ishiguro <t10078si@sfc.keio.ac.jp>'
__copyright__ = ''
__license__ = ''

from genbank_generator import Genbank
#from genbank_generator import Promoter
#from genbank_generator import Terminater


class AnnotationBuilder(object):
    def __init__(self):
        pass

    def generate_annotations(self):
        gb = Genbank()
        gb.generate_genbank_db()

        #promoter = Promoter()
        #promoter.genrate_promoter_db()

    
if __name__ == '__main__':
    builder = AnnotationBuilder()
    builder.generate_annotations()
    print "finished parsing"
