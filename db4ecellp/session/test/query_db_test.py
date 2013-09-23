import sys
sys.path.append('../')

from session import QueryBuilder

conf = '../../../conf.ini'
q = QueryBuilder(conf)
print q.include_gene_in_region(3390, 8000)



