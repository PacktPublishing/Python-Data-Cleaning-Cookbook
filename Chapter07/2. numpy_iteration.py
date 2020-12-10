# import pandas and numpy, and load the covid data
import pandas as pd
import numpy as np
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
coviddaily = pd.read_csv("data/coviddaily720.csv", parse_dates=["casedate"])
ltbrazil = pd.read_csv("data/ltbrazil.csv")

# create a list of locations
loclist = coviddaily.location.unique().tolist()

# use a numpy array to calculate sums
rowlist = []
casevalues = coviddaily[['location','new_cases']].to_numpy()
for locitem in loclist:
  cases = [casevalues[j][1] for j in range(len(casevalues))\
    if casevalues[j][0]==locitem]
  rowlist.append(sum(cases))

len(rowlist)
len(loclist)
rowlist[0:5]
casetotals = pd.DataFrame(zip(loclist,rowlist), columns=(['location','casetotals']))
casetotals.head()

# sort the land temperatures data and drop rows with missing values for temperature
ltbrazil = ltbrazil.sort_values(['station','month'])
ltbrazil = ltbrazil.dropna(subset=['temperature'])

# iterate using numpy arrays
prevstation = 'ZZZ'
prevtemp = 0
rowlist = []
tempvalues = ltbrazil[['station','temperature']].to_numpy()
for j in range(len(tempvalues)):
  station = tempvalues[j][0]
  temperature = tempvalues[j][1]
  if (prevstation!=station):
    if (prevstation!='ZZZ'):
      rowlist.append({'station':prevstation, 'avgtemp':tempcnt/stationcnt, 'stationcnt':stationcnt})
    tempcnt = 0
    stationcnt = 0
    prevstation = station
  
  if ((0 <= abs(temperature-prevtemp) <= 3) or (stationcnt==0)):
    tempcnt += temperature
    stationcnt += 1
  
  prevtemp = temperature

rowlist.append({'station':prevstation, 'avgtemp':tempcnt/stationcnt, 'stationcnt':stationcnt})
rowlist[0:5]

# create a data frame of land temperature averages
ltbrazilavgs = pd.DataFrame(rowlist)
ltbrazilavgs.head()
