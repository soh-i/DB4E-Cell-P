E-Cell4 P: Database project for whole cell simulation in _E. coli_.
===========
## Description 
Providing generating database class and query/filter DB interfaces for running simulation model

## Setup
### Install dependencies
pip install -r requeirements.txt

### How to generate SQLite DB
put Required files in "data" folder and 
create folder named "db"

## Running
### Query genome sequence and annotations
```python
from session import Mapper, Query
query = Query()

print query.count_stored_records()
#=> 4145
print query.collect_cds_records()
#=> return All CDS annotations ans its sequences
print query.find_by_name('thrL')
#=> <Species('thrL','1','189','255','CDS','ATGAAACGCATTACCACCACCAT...')>
print query.collect_annotations_filter_by_strand(-1)
#=> return annotations and sequence on complement strand
print query.include_gene_in_region(21, 2012)
#=> [u'thrL', u'thrA']
```
