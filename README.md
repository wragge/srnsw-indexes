# SRNSW Index Harvester

This code extracts data from the indexes published online in tabular form by State Records NSW and saves them as CSV files.

View a [list of the available indexes](https://www.records.nsw.gov.au/archives/collections-and-research/guides-and-indexes/indexes-a-z) on the SRNSW site.

To create a list of all the available indexes and their urls, do:


``` python

import indexes
indexes.list_indexes()

```

This generates a [CSV file](data/indexes.csv) listing the index name and url.

To harvest all the indexes you can do:

``` python

import indexes
indexes.get_all_indexes()
```

To harvest an individual index, find the one you want in the [indexes.csv](data/indexes.csv) file and copy the row. The you can do:

``` python
import harvest
harvest.get_index([past the row in here])
```

So for example:

``` python
import harvest
harvest.get_index(["Criminal Jurisdiction","http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Criminal Jurisdiction&id=57&frm=1&query=Names:%"])
```

The [results of the above harvest](data/criminal-jurisdiction.csv) are in the data directory.

Note that I haven't yet tested this across all indexes (some are very big). As I harvest them I'll add them to the data directory.

