# SRNSW Index Harvester

Here you'll code to harvest data from the indexes published online by State Records NSW and save them as CSV files. 

I've pre-harvested all the current indexes for your convenience. You can browse them below, or poke around in the `data` directory. You can also download a [zip file](https://github.com/wragge/srnsw-indexes/archive/master.zip) (about 25mb) containing the complete repository

There are more [details about the available indexes](https://www.records.nsw.gov.au/archives/collections-and-research/guides-and-indexes/indexes-a-z) on the SRNSW site.

Thanks to the SRNSW staff and volunteers for preparing all this most excellent data.

## Harvested indexes

**Currently: 58 indexes harvested with 929,104 rows of data.**

| Name | Number of rows | Download data | View at SRNSW |
|------|----------------|---------------|---------------|
| Aboriginal cases | 56 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/aboriginal-cases.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Aboriginal cases&id=1&frm=1&query=Names:%) |
| Applications to Marry | 4154 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/applications-to-marry.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Applications to Marry&id=68&frm=1&query=[Applicant (Male)]:%) |
| Assisted Immigrants | 191909 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/assisted-immigrants.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Assisted Immigrants&id=9&frm=1&query=Surname:%) |
| Australian Railway Supply Detachment | 65 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/australian-railway-supply-detachment.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Australian Railway Supply Detachment&id=8&frm=1&query=Surname:%) |
| Bankruptcy Index | 28880 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/bankruptcy-index.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Bankruptcy Index&id=59&frm=1&query=Surname:%) |
| Bench of Magistrates cases, 1788-1820 | 4442 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/bench-of-magistrates-cases-1788-1820.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Bench of Magistrates cases, 1788-1820&id=11&frm=1&query=Surname:%) |
| CSreLand | 10849 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/csreland.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=CSreLand&id=14&frm=1&query=Surname:%) |
| Child Care and Protection | 21980 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/child-care-and-protection.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Child Care and Protection&id=74&frm=1&query=Surname:%) |
| Closer Settlement Transfer Registers, NRS 8082 | 4957 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/closer-settlement-transfer-registers-nrs-8082.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Closer Settlement Transfer Registers, NRS 8082&id=62&frm=1&query=Surname:%) |
| Closer and Soldier Settlement Transfer Files | 4503 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/closer-and-soldier-settlement-transfer-files.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Closer and Soldier Settlement Transfer Files&id=41&frm=1&query=Surname:%) |
| Colonial Secretary Main series of letters received,1826-1982 | 7638 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/colonial-secretary-main-series-of-letters-received-1826-1982.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Colonial Secretary Main series of letters received,1826-1982&id=45&frm=1&query=Year:%) |
| Convict Index | 141854 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/convict-index.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Convict Index&id=65&frm=1&query=Surname:%) |
| Coroners Inquests 1796-1824 | 808 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/coroners-inquests-1796-1824.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Coroners Inquests 1796-1824&id=61&frm=1&query=Surname:%) |
| Court of Civil Jurisdiction index | 2876 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/court-of-civil-jurisdiction-index.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Court of Civil Jurisdiction index&id=42&frm=1&query=Plaintiff:%) |
| Criminal Jurisdiction | 5028 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/criminal-jurisdiction.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Criminal Jurisdiction&id=57&frm=1&query=Names:%) |
| Depasturing Licenses | 7449 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/depasturing-licenses.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Depasturing Licenses&id=67&frm=1&query=Surname:%) |
| Divorce Index | 21240 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/divorce-index.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Divorce Index&id=16&frm=1&query=Surname:%) |
| Early Convict Index | 12652 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/early-convict-index.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Early Convict Index&id=77&frm=1&query=Surname:%) |
| FieldBooks | 813 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/fieldbooks.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=FieldBooks&id=17&frm=1&query=Surname:%) |
| Government Architect | 2382 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/government-architect.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Government Architect&id=64&frm=1&query=Place:%) |
| Government Asylums for the Infirm and Destitute | 10264 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/government-asylums-for-the-infirm-and-destitute.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Government Asylums for the Infirm and Destitute&id=80&frm=1&query=Surname:%) |
| Governor’s Court Case Papers, 1815-1824 | 3789 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/governor-s-court-case-papers-1815-1824.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Governor’s Court Case Papers, 1815-1824&id=76&frm=1&query=Surname:%) |
| Index on Occupants on Aboriginal Reserves, 1875 to 1904 | 68 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-on-occupants-on-aboriginal-reserves-1875-to-1904.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index on Occupants on Aboriginal Reserves, 1875 to 1904&id=47&frm=1&query=Surname:%) |
| Index to 1841 Census | 9355 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-1841-census.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index to 1841 Census&id=18&frm=1&query=Surname:%) |
| Index to Closer Settlement Promotion | 4354 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-closer-settlement-promotion.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index to Closer Settlement Promotion&id=60&frm=1&query=Surname:%) |
| Index to Court of Claims | 1048 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-court-of-claims.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index to Court of Claims&id=54&frm=1&query=Surname:%) |
| Index to Deposition Registers | 65789 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-deposition-registers.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index to Deposition Registers&id=40&frm=1&query=Surname:%) |
| Index to Early Probate Records | 1627 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-early-probate-records.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index to Early Probate Records&id=52&frm=1&query=Surname:%) |
| Index to Gaol Photographs | 47629 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-gaol-photographs.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index to Gaol Photographs&id=22&frm=1&query=Surname:%) |
| Index to Intestate Estate Case Papers | 21474 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-intestate-estate-case-papers.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index to Intestate Estate Case Papers&id=53&frm=1&query=Surname:%) |
| Index to Miscellaneous Immigrants | 8821 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-miscellaneous-immigrants.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index to Miscellaneous Immigrants&id=55&frm=1&query=Surname:%) |
| Index to Quarter Sessions cases, 1824-37 | 6232 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-quarter-sessions-cases-1824-37.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index to Quarter Sessions cases, 1824-37&id=25&frm=1&query=Surname:%) |
| Index to Registers of Firms | 45683 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-registers-of-firms.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index to Registers of Firms&id=48&frm=1&query=[Name of Firm]:%) |
| Index to Squatters and Graziers | 8981 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-squatters-and-graziers.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index to Squatters and Graziers&id=70&frm=1&query=Surname:%) |
| Index to Vessels Arrived, 1837 - 1925 | 120133 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-vessels-arrived-1837-1925.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index to Vessels Arrived, 1837 - 1925&id=49&frm=1&query=[Ship Name]:%) |
| Index to convict exiles, 1846-50 | 3036 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-convict-exiles-1846-50.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index to convict exiles, 1846-50&id=20&frm=1&query=Surname:%) |
| Index to the Unassisted Arrivals NSW 1842-1855 | 136105 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-the-unassisted-arrivals-nsw-1842-1855.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Index to the Unassisted Arrivals NSW 1842-1855&id=43&frm=1&query=Names:%) |
| Insolvency Index | 23108 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/insolvency-index.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Insolvency Index&id=10&frm=1&query=Surname:%) |
| King’s and Queen’s Counsel Appointments | 1986 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/king-s-and-queen-s-counsel-appointments.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=King’s and Queen’s Counsel Appointments&id=83&frm=1&query=Surname:%) |
| LandGrants | 5627 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/landgrants.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=LandGrants&id=78&frm=1&query=Surname:%) |
| List of Maps and Plans (and Supplement) | 5871 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/list-of-maps-and-plans-and-supplement-.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=List of Maps and Plans (and Supplement)&id=33&frm=1&query=[SR Item]:%) |
| NSW Chemists and Druggists | 2967 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/nsw-chemists-and-druggists.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=NSW Chemists and Druggists&id=72&frm=1&query=Surname:%) |
| NSW Government Employees Granted Military Leave, 1914-1918 | 13735 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/nsw-government-employees-granted-military-leave-1914-1918.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=NSW Government Employees Granted Military Leave, 1914-1918&id=82&frm=1&query=Surname:%) |
| NSW Govt Railways and Tramways - Roll of Honour - 1914-1919 | 1214 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/nsw-govt-railways-and-tramways-roll-of-honour-1914-1919.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=NSW Govt Railways and Tramways - Roll of Honour - 1914-1919&id=46&frm=1&query=Surname:%) |
| Naturalisation | 9860 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/naturalisation.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Naturalisation&id=30&frm=1&query=Surname:%) |
| Nominal Roll of the First Railway Section (AIF) | 435 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/nominal-roll-of-the-first-railway-section-aif-.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Nominal Roll of the First Railway Section (AIF)&id=7&frm=1&query=Surname:%) |
| Publicans Licenses | 18457 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/publicans-licenses.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Publicans Licenses&id=69&frm=1&query=Surname:%) |
| Railway Employment Records | 763 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/railway-employment-records.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Railway Employment Records&id=50&frm=1&query=Surname:%) |
| Register of Auriferous Leases | 35150 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/register-of-auriferous-leases.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Register of Auriferous Leases&id=63&frm=1&query=Surname:%) |
| Registers of Nurses | 10691 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/registers-of-nurses.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Registers of Nurses&id=79&frm=1&query=Surname:%) |
| Registers of Police | 11319 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/registers-of-police.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Registers of Police&id=31&frm=1&query=Surname:%) |
| Registers of Settlement Purchases | 9776 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/registers-of-settlement-purchases.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Registers of Settlement Purchases&id=58&frm=1&query=Surname:%) |
| Returned Soldier Settlement Loan Files | 7642 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/returned-soldier-settlement-loan-files.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Returned Soldier Settlement Loan Files&id=75&frm=1&query=Surname:%) |
| Returned Soldiers Settlement Misc files 1916-25 | 1052 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/returned-soldiers-settlement-misc-files-1916-25.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Returned Soldiers Settlement Misc files 1916-25&id=56&frm=1&query=Surname:%) |
| Schools | 21245 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/schools.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Schools&id=32&frm=1&query=School:%) |
| Surveyor General - Letters received 1822-55 | 156 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/surveyor-general-letters-received-1822-55.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Surveyor General - Letters received 1822-55&id=35&frm=1&query=Surname:%) |
| Teachers Rolls | 14867 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/teachers-rolls.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Teachers Rolls&id=73&frm=1&query=Surname:%) |
| Unemployed in Sydney 1866 | 3222 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/unemployed-in-sydney-1866.csv) | [Web site](http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Unemployed in Sydney 1866&id=81&frm=1&query=Surname:%) |


## Create your own harvest

You'll need to have [Robobrowser](https://github.com/jmcarp/robobrowser) installed.

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
harvest.get_index([paste the row in here])
```

So for example:

``` python
import harvest
harvest.get_index(["Criminal Jurisdiction","http://indexes.records.nsw.gov.au/searchhits_nocopy.aspx?table=Criminal Jurisdiction&id=57&frm=1&query=Names:%"])
```

The [results of the above harvest](data/criminal-jurisdiction.csv) are in the data directory.


