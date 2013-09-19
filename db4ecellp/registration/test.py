#!/usr/bin/env python 

from session import Mapper, Query


def query_test():

    # create Mapper class object
    query = Query()
    print "Mapping CDS table to DB is finished..."
    
    #print mapper.retrieve_all_records()
    #print mapper.query_by_all_cds()
    #print mapper.query_by_gene_name('thrL')
    #print mapper.query_by_region(189, 12255)
    #print mapper.query_by_region_with_gene(1,3010)
    #print mapper.query_by_region_with_seq(1,3010)
    #print mapper.collect_all_annotations_by_strand(1)
    print query.include_gene_in_region(21, 2012)


if __name__ == '__main__':
    query_test()
