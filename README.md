# SRNSW Index Harvester

This repository provides code to harvest data from the indexes published online by State Records NSW and save them as CSV files. 

Copies of the harvested CSV files are available in the `data` directory.

View a [list of the available indexes](https://www.records.nsw.gov.au/archives/collections-and-research/guides-and-indexes/indexes-a-z) on the SRNSW site.

## Harvested indexes

| Index | Number of rows |
|-------|----------------|
| [Aboriginal cases](data/aboriginal-cases.csv) | 56 |
| [Applications to Marry](data/applications-to-marry.csv) | 4154 |
| [Assisted Immigrants](data/assisted-immigrants.csv) | 191909 |
| [Australian Railway Supply Detachment](data/australian-railway-supply-detachment.csv) | 65 |
| [Bankruptcy Index](data/bankruptcy-index.csv) | 28880 |
| [Bench of Magistrates cases, 1788-1820](data/bench-of-magistrates-cases-1788-1820.csv) | 4442 |
| [CSreLand](data/csreland.csv) | 10849 |
| [Child Care and Protection](data/child-care-and-protection.csv) | 21980 |
| [Closer Settlement Transfer Registers, NRS 8082](data/closer-settlement-transfer-registers-nrs-8082.csv) | 4957 |
| [Closer and Soldier Settlement Transfer Files](data/closer-and-soldier-settlement-transfer-files.csv) | 4503 |
| [Colonial Secretary Main series of letters received,1826-1982](data/colonial-secretary-main-series-of-letters-received-1826-1982.csv) | 7638 |
| [Convict Index](data/convict-index.csv) | 141854 |
| [Coroners Inquests 1796-1824](data/coroners-inquests-1796-1824.csv) | 808 |
| [Court of Civil Jurisdiction index](data/court-of-civil-jurisdiction-index.csv) | 2876 |
| [Criminal Jurisdiction](data/criminal-jurisdiction.csv) | 5028 |
| [Depasturing Licenses](data/depasturing-licenses.csv) | 7449 |
| [Divorce Index](data/divorce-index.csv) | 21240 |
| [Early Convict Index](data/early-convict-index.csv) | 12652 |
| [FieldBooks](data/fieldbooks.csv) | 813 |
| [Government Architect](data/government-architect.csv) | 2382 |
| [Government Asylums for the Infirm and Destitute](data/government-asylums-for-the-infirm-and-destitute.csv) | 10264 |
| [Governor’s Court Case Papers, 1815-1824](data/governor-s-court-case-papers-1815-1824.csv) | 3789 |
| [Index on Occupants on Aboriginal Reserves, 1875 to 1904](data/index-on-occupants-on-aboriginal-reserves-1875-to-1904.csv) | 68 |
| [Index to 1841 Census](data/index-to-1841-census.csv) | 9355 |
| [Index to Closer Settlement Promotion](data/index-to-closer-settlement-promotion.csv) | 4354 |
| [Index to Court of Claims](data/index-to-court-of-claims.csv) | 1048 |
| [Index to Deposition Registers](data/index-to-deposition-registers.csv) | 65789 |
| [Index to Early Probate Records](data/index-to-early-probate-records.csv) | 1627 |
| [Index to Gaol Photographs](data/index-to-gaol-photographs.csv) | 47629 |
| [Index to Intestate Estate Case Papers](data/index-to-intestate-estate-case-papers.csv) | 21474 |
| [Index to Miscellaneous Immigrants](data/index-to-miscellaneous-immigrants.csv) | 8821 |
| [Index to Quarter Sessions cases, 1824-37](data/index-to-quarter-sessions-cases-1824-37.csv) | 6232 |
| [Index to Registers of Firms](data/index-to-registers-of-firms.csv) | 45683 |
| [Index to Squatters and Graziers](data/index-to-squatters-and-graziers.csv) | 8981 |
| [Index to Vessels Arrived, 1837 - 1925](data/index-to-vessels-arrived-1837-1925.csv) | 120133 |
| [Index to convict exiles, 1846-50](data/index-to-convict-exiles-1846-50.csv) | 3036 |
| [Index to the Unassisted Arrivals NSW 1842-1855](data/index-to-the-unassisted-arrivals-nsw-1842-1855.csv) | 136105 |
| [Insolvency Index](data/insolvency-index.csv) | 23108 |
| [King’s and Queen’s Counsel Appointments](data/king-s-and-queen-s-counsel-appointments.csv) | 1986 |
| [LandGrants](data/landgrants.csv) | 5627 |
| [List of Maps and Plans (and Supplement)](data/list-of-maps-and-plans-and-supplement-.csv) | 5871 |
| [NSW Chemists and Druggists](data/nsw-chemists-and-druggists.csv) | 2967 |
| [NSW Government Employees Granted Military Leave, 1914-1918](data/nsw-government-employees-granted-military-leave-1914-1918.csv) | 13735 |
| [NSW Govt Railways and Tramways - Roll of Honour - 1914-1919](data/nsw-govt-railways-and-tramways-roll-of-honour-1914-1919.csv) | 1214 |
| [Naturalisation](data/naturalisation.csv) | 9860 |
| [Nominal Roll of the First Railway Section (AIF)](data/nominal-roll-of-the-first-railway-section-aif-.csv) | 435 |
| [Publicans Licenses](data/publicans-licenses.csv) | 18457 |
| [Railway Employment Records](data/railway-employment-records.csv) | 763 |
| [Register of Auriferous Leases](data/register-of-auriferous-leases.csv) | 35150 |
| [Registers of Nurses](data/registers-of-nurses.csv) | 10691 |
| [Registers of Police](data/registers-of-police.csv) | 11319 |
| [Registers of Settlement Purchases](data/registers-of-settlement-purchases.csv) | 9776 |
| [Returned Soldier Settlement Loan Files](data/returned-soldier-settlement-loan-files.csv) | 7642 |
| [Returned Soldiers Settlement Misc files 1916-25](data/returned-soldiers-settlement-misc-files-1916-25.csv) | 1052 |
| [Schools](data/schools.csv) | 21245 |
| [Surveyor General - Letters received 1822-55](data/surveyor-general-letters-received-1822-55.csv) | 156 |
| [Teachers Rolls](data/teachers-rolls.csv) | 14867 |
| [Unemployed in Sydney 1866](data/unemployed-in-sydney-1866.csv) | 3222 |


## Create your own harvest

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


