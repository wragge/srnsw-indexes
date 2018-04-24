# SRNSW Index Harvester

Here you'll find code to harvest data from the indexes published online by State Records NSW and save them as CSV files.

I've pre-harvested all the current indexes for your convenience. You can browse them below, or poke around in the `data` directory. You can also download a [zip file](https://github.com/wragge/srnsw-indexes/archive/master.zip) (about 54mb) containing the complete repository.

The repository includes two versions of each index. The web layout of the indexes on the State Archives site includes a number of empty columns. I've harvested and saved these as they are, but I have also created a 'cleaned' version with the unnecessary columns removed. Both versions are provided so you can check that nothing important has been lost in the cleaning process.

One index, the 'Early Convict Index', is linked on the State Archives site to an [old version](http://indexes.records.nsw.gov.au/searchform.aspx?id=77), however, a [new version](https://www.records.nsw.gov.au/searchhits_nocopy?id=77&surname=%25&firstname=&alias=&tried_at=0&county=0&tried%20when=0&sentence=0&ship=0&ship%20page=&remarks=) exists and this is the version I've harvested. Strangely, my harvest results in more rows than seem to be present on the site. I'm not sure why this is.

There are more [details about the available indexes](https://www.records.nsw.gov.au/archives/collections-and-research/guides-and-indexes/indexes-a-z) on the SRNSW site.

Thanks to the SRNSW staff and volunteers for preparing all this most excellent data.

SRNSW content in copyright is licensed under a [Creative Commons Attribution 4.0 International (CC BY 4.0) licence](http://creativecommons.org/licenses/by/4.0/). See their [copyright page](https://www.records.nsw.gov.au/about-state-records/copyright-policy) for more information.

## Harvested indexes

**Currently: 60 indexes harvested with 1,488,222 rows rows of data.**

| Name | Number of rows | Download data | View at SRNSW |
|------|----------------|---------------|---------------|
| Assisted Immigrants | 191688 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/assisted-immigrants.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=9&surname=%25&firstname=&ship=0&year=&arriving=0&remarks=) |
| Australian Railway Supply Detachment | 65 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/australian-railway-supply-detachment.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=8&surname=%25&firstname=) |
| Bankruptcy Index | 28880 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/bankruptcy-index.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=59&surname=%25&firstname=&date%20of%20trial=&occupation=&date%20of%20sequestration=&business=) |
| Bench of Magistrates cases, 1788-1820 | 4442 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/bench-of-magistrates-cases-1788-1820.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=11&surname=%25&firstname=&charge%20or%20nature%20of%20document=&date=) |
| CSreLand | 10849 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/csreland.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=14&surname=%25&firstname=&1stdate=&remarks=) |
| Child Care and Protection | 21980 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/child-care-and-protection.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=74&surname=%25&firstname=&committal%20date=&institution=0&remarks=) |
| Closer Settlement Transfer Registers, NRS 8082 | 4957 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/closer-settlement-transfer-registers-nrs-8082.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=62&surname=%25&firstname=&surname%20of%20transferee=&firstname%20of%20transferee=&name%20of%20estate=&settlement%20purchase%20no=&land%20district=&date%20of%20transfer=) |
| Closer and Soldier Settlement Transfer Files | 4503 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/closer-and-soldier-settlement-transfer-files.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=41&surname=%25&firstname=&residence%20of%20owner=&settlement%20purchase%20area=&county=&parish=) |
| Colonial Secretary Main series of letters received,1826-1982 | 7638 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/colonial-secretary-main-series-of-letters-received-1826-1982.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=45&year=%25&title=&place=&minister=&church=) |
| Convict Index | 141854 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/convict-index.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=65&surname=%25&firstname=&alias=&remarks=&recordtype=0&vessel=0&year=) |
| Convicts Applications to Marry 1825-51 | 5770 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/convicts-applications-to-marry-1825-51.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=68&applicant%20%28male%29=%25&ship%20%28male%29=&applicant%20%28female%29=&ship%20%28female%29=&date%20of%20permission=&place=) |
| Coroners Inquests 1796-1824 | 808 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/coroners-inquests-1796-1824.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=61&surname=%25&firstname=&date=&remarks=) |
| Court of Civil Jurisdiction index | 2876 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/court-of-civil-jurisdiction-index.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=42&plaintiff=%25&defendant=&date=) |
| Criminal Court Records index 1788-1833 | 5028 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/criminal-court-records-index-1788-1833.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=57&names=%25&offence=&date=) |
| Criminal Indictments, 1863-1919 | 15701 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/criminal-indictments-1863-1919.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=86&Surname=%25&Firstname=&Alias=&Offence=&Where%20Tried&Date%20of%20Trial) |
| Deceased Estates | 267945 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/deceased-estates.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=15&surname=%25&firstname=&locality=&dateofdeath=&datedutypaid=) |
| Depasturing Licenses | 7449 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/depasturing-licenses.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=67&names=%25&offence=&date%20of%20trial=) |
| Divorce Index | 21240 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/divorce-index.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=16&surname=%25&firstname=&respondent%20surname=&respondent%20firstname=&co-respondent%20surname=&co-respondent%20firstName=&year=) |
| Early Convict Index | 12940 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/early-convict-index.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=77&surname=%25&firstname=&alias=&tried_at=0&county=0&tried%20when=0&sentence=0&ship=0&ship%20page=&remarks=) |
| FieldBooks | 813 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/fieldbooks.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=17&surname=%25&firstname=&locality=) |
| Government Architect | 2373 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/government-architect.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=64&place=%25&description=&date=&remarks=&recordtype=0) |
| Government Asylums for the Infirm and Destitute | 10264 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/government-asylums-for-the-infirm-and-destitute.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=80&surname=%25&firstname=&institution=0) |
| Governor’s Court Case Papers, 1815-1824 | 3790 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/governor-s-court-case-papers-1815-1824.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=76&surname=%25&firstname=&year=&item%20no=&case%20no=&series%20no=) |
| Index on Occupants on Aboriginal Reserves, 1875 to 1904 | 80 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-on-occupants-on-aboriginal-reserves-1875-to-1904.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=47&surname=%25&firstname=&location=) |
| Index to 1841 Census | 9355 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-1841-census.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=18&surname=%25&firstname=&residence=) |
| Index to Closer Settlement Promotion | 4354 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-closer-settlement-promotion.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=60&surname=%25&firstname=&vendors%20surname=&vendors%20first%20name=&land%20district=&estate%2Ffarm%20name=&previous%20system%20number=&csp%20no=) |
| Index to Court of Claims | 1052 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-court-of-claims.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=54&surname=%25&firstname=&first%20possessor%20of%20land=&address=) |
| Index to Deposition Registers | 65790 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-deposition-registers.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=40&surname=%25&firstname=&place%20of%20committal=&committed%20for%20trial%20at=&date%20of%20committal=&alleged%20offence=) |
| Index to Early Probate Records | 1627 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-early-probate-records.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=52&surname=%25&firstname=&date=) |
| Index to Gaol Photographs | 48171 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-gaol-photographs.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=84&surname=%25&firstname=&birthplace=&dateofphoto=&gaol=&photono=&startdate=&enddate=) |
| Index to Intestate Estate Case Papers | 22520 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-intestate-estate-case-papers.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=53&surname=%25&firstname=&alias=&number=&district=&location=) |
| Index to Miscellaneous Immigrants | 8821 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-miscellaneous-immigrants.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=55&surname=%25&firstname=&ship=&date=) |
| Index to Quarter Sessions cases, 1824-37 | 6232 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-quarter-sessions-cases-1824-37.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=25&surname=%25&firstname=&place=) |
| Index to Registers of Firms | 45683 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-registers-of-firms.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=48&name%20of%20firm=%25&nature%20of%20business=&place%20of%20business=&person%20carrying%20on%20business=&additional%20people%20in%20business=) |
| Index to Squatters and Graziers | 9003 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-squatters-and-graziers.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=70&surname=%25&firstname=&station=&date=&description=) |
| Index to Vessels Arrived, 1837 - 1925 | 120083 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-vessels-arrived-1837-1925.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=49&ship%20name=%25&year=&month=0) |
| Index to convict exiles, 1846-50 | 3036 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-convict-exiles-1846-50.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=20&surname=%25&firstname=&ship=&trialshire=&trialcity%2Ftown=&tldistrict=) |
| Index to the Unassisted Arrivals NSW 1842-1855 | 135792 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/index-to-the-unassisted-arrivals-nsw-1842-1855.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=43&names=%25&ship=&date%20of%20arrival=&origin%20port=) |
| Indigenous Colonial Court Cases 1788-1838 | 66 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/indigenous-colonial-court-cases-1788-1838.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=1&names=%25&offence=&date%20of%20trial=&where%20tried=) |
| Insolvency Index | 23108 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/insolvency-index.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=10&surname=%25&firstname=&locality=&occupation=&sequestration=&business=) |
| King’s and Queen’s Counsel Appointments | 2083 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/king-s-and-queen-s-counsel-appointments.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=83&surname=%25&firstname=&year%20appointed%20silk=) |
| LandGrants | 5627 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/landgrants.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=78&surname=%25&firstname=&district%2Flocality=&years=) |
| List of Maps and Plans (and Supplement) | 5455 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/list-of-maps-and-plans-and-supplement-.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=33&and%20supplement%20%28sa%20item%29=%25&sg%20map=&surname=&area=&description=&date=) |
| NSW Chemists and Druggists | 2967 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/nsw-chemists-and-druggists.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=72&surname=%25&firstname=&date%20of%20registration=&residence=) |
| NSW Government Employees Granted Military Leave, 1914-1918 | 13735 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/nsw-government-employees-granted-military-leave-1914-1918.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=82&surname=%25&firstname=&position=&department=&branch=&status=&military%20unit=&remarks=) |
| NSW Govt Railways and Tramways - Roll of Honour - 1914-1919 | 1214 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/nsw-govt-railways-and-tramways-roll-of-honour-1914-1919.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=46&surname=%25&firstname=&branch=&military%20unit=) |
| Naturalisation | 9860 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/naturalisation.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=30&surname=%25&firstname=&nativeplace=&dateofcertificate=) |
| Nominal Roll of the First Railway Section (AIF) | 417 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/nominal-roll-of-the-first-railway-section-aif-.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=7&surname=%25&othernames=&age=&address=) |
| Publicans Licenses | 18457 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/publicans-licenses.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=69&surname=%25&firstname=&hotel=&locality=&year=&remarks=) |
| Railway Employment Records | 763 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/railway-employment-records.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=50&surname=%25&firstname=&first%20position%20listed=&date%20of%20first%20position%20listed=) |
| Register of Auriferous Leases | 53076 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/register-of-auriferous-leases.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=63&surname=%25&firstname=&company=&location%20of%20lease=&date%20of%20application=&remarks=) |
| Registers of Nurses | 26665 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/registers-of-nurses.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=79&surname=%25&firstname=&type%20of%20nurse=&date%20of%20registration=) |
| Registers of Police | 11319 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/registers-of-police.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=31&surname=%25&firstname=&nativeof=&dateappointed=) |
| Registers of Settlement Purchases | 9776 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/registers-of-settlement-purchases.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=58&surname=%25&firstname=&land%20district=&date%20of%20selection=) |
| Returned Soldier Settlement Loan Files | 7642 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/returned-soldier-settlement-loan-files.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=75&surname=%25&firstname=&land%20district=) |
| Returned Soldiers Settlement Misc files 1916-25 | 1050 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/returned-soldiers-settlement-misc-files-1916-25.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=56&surname=%25&firstname=&class%20of%20holding=&land%20district=) |
| Schools | 21245 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/schools.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=32&school=%25&date=&item=&remarks=) |
| Surveyor General - Letters received 1822-55 | 156 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/surveyor-general-letters-received-1822-55.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=35&surname=%25&firstname=&locality=) |
| Teachers Rolls | 14867 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/teachers-rolls.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=73&surname=%25&firstname=&remarks=) |
| Unemployed in Sydney 1866 | 3222 | [CSV file](https://github.com/wragge/srnsw-indexes/raw/master/data/unemployed-in-sydney-1866.csv) | [Web site](https://www.records.nsw.gov.au/searchhits_nocopy?id=81&surname=%25&firstname=&occupation=) |


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
