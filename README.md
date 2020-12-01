# taicol-test
#### Installing 

To install <project_, follow these steps:

Production:
```
docker-compose -f docker-compose-off.yml build
```

Development:
```
docker-compose build
```

#### How to use it
# Taicol API handbook
Webisite URL: http://api.taicol.tw:8080/

![](https://i.imgur.com/tUNGjrE.png)

#### List completed dataset 
1. namecode: http://api.taicol.tw:8080/namecode/
2. scientific name: http://api.taicol.tw:8080/speciesname/
3. common name: http://api.taicol.tw:8080/common/

#### Find the certain data from ==namecode==

* Find the species by namecode: enter your namecode (ex:403245)
`http://api.taicol.tw:8080/namecode/403245`
* Generate the simple format : enter simple=True or False, default is False
`http://api.taicol.tw:8080/namecode/403245/simple=True`

:::info
Simple format only retains name_code, name, is_endemic, alien_status, comment, datelastmodified, family, family_c, common_name_c, iucn_code, cites_code, coa_redlist_code, redlist_tw_2017
:::

#### Find the certain data from ==scientific name==

* Find the species by scientific name: no need to enter completed name (ex: Aulodrilus pigueti or pigueti)
`http://api.taicol.tw:8080/speciesname/Aulodrilus pigueti`
* Add additional criterias:
  + update date : enter date=YYYY-MM-DD (ex:2011-01-09)
  `http://api.taicol.tw:8080/speciesname/Aulodrilus pigueti/date=2011-01-09`
  + is accepted name: enter accept=True or False
  `http://api.taicol.tw:8080/speciesname/Aulodrilus pigueti/accept=True`
:::info
Update date: find certain species since update date
Is accept name: check whether species is accepted name or not 
:::
* Generate the simple format : enter simple=True or False, default is False
`http://api.taicol.tw:8080/speciesname/Aulodrilus pigueti/simple=True`
* Combine above-mentioned criterias: date first, then accept, simple at last
`http://api.taicol.tw:8080/speciesname/Aulodrilus/date=2012-01-01/accept=True/simple=True`

#### Find the certain data from ==common name==
* Find the species by common name: no need to enter completed name (ex: Aulodrilus pigueti or pigueti)
`http://api.taicol.tw:8080/common/山柑`
* Add additional criterias:
  + update date : enter date=YYYY-MM-DD (ex:2011-01-09)
  `http://api.taicol.tw:8080/common/山柑/date=2011-01-09`
  + is accepted name: enter accept=True or False
  `http://api.taicol.tw:8080/common/山柑/accept=True`
* Generate the simple format : enter simple=True or False, default is False
`http://api.taicol.tw:8080/common/山柑/simple=True`
* Combine above-mentioned criterias: date first, then accept, simple at last
`http://api.taicol.tw:8080//common/山柑/date=2012-01-01/accept=True/simple=True`
