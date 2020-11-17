# import pandas, numpy, json, pprint, and requests
import pandas as pd
import numpy as np
import json
import pprint
import requests
from bs4 import BeautifulSoup

pd.set_option('display.width', 80)
pd.set_option('display.max_columns',6)

# parse the web page and get the header row of the table

webpage = requests.get("http://www.alrb.org/datacleaning/covidcaseoutliers.html")
bs = BeautifulSoup(webpage.text, 'html.parser')
theadrows = bs.find('table', {'id':'tblDeaths'}).thead.find_all('th')
type(theadrows)
labelcols = [j.get_text() for j in theadrows]
labelcols[0] = "rowheadings"
labelcols

# get the data from the table cells
rows = bs.find('table', {'id':'tblDeaths'}).tbody.find_all('tr')
datarows = []
labelrows = []
for row in rows:
  rowlabels = row.find('th').get_text()
  cells = row.find_all('td', {'class':'data'})
  if (len(rowlabels)>3):
    labelrows.append(rowlabels)
  if (len(cells)>0):
    cellvalues = [j.get_text() for j in cells]
    datarows.append(cellvalues)

pprint.pprint(datarows[0:2])
pprint.pprint(labelrows[0:2])

for i in range(len(datarows)):
  datarows[i].insert(0, labelrows[i])

pprint.pprint(datarows[0:2])

# load the data into pandas
totaldeaths = pd.DataFrame(datarows, columns=labelcols)
totaldeaths.iloc[:,1:5].head()
totaldeaths.dtypes
totaldeaths.columns = totaldeaths.columns.str.replace(" ", "_").str.lower()

for col in totaldeaths.columns[1:-1]:
  totaldeaths[col] = totaldeaths[col].\
    str.replace("[^0-9]","").astype('int64')

totaldeaths['hospital_beds_per_100k'] = totaldeaths['hospital_beds_per_100k'].astype('float')
totaldeaths.head()
totaldeaths.dtypes

