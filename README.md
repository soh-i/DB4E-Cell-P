E-Cell4 P: Database project for whole cell simulation in _E. coli_
===========
## Description 
Providing generating database class and query/filter DB interfaces for running simulation model

## Installation
### Install dependencies
```
pip install -r requeirements.txt
```

### Required data
Some required RegulonDB/refSeq dataset are able to download by `misc/required_data_downloader.pl`, then put those files into `data` directory.

* NC_000913.gbk
* PromoterSet.txt
* TerminatorSet.txt

### Configuration file
Add **absolute** project root path into `conf.ini`.
```ini
[root]
APP_ROOT=/Users/yukke/dev/DB4E-Cell-P
```

## Running
Sample code is `query_test.py` in `DB4E-Cell-P/db4ecellp` directory.

### Query genome sequence and annotations
```python
from db4ecellp import db4ecellp
query = db4ecellp.Query('./conf.ini') # PATH TO conf.ini

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
