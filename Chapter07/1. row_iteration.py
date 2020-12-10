# import pandas and numpy, and load the covid data
import pandas as pd
import numpy as np
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
coviddaily = pd.read_csv("data/coviddaily720.csv", parse_dates=["casedate"])
ltbrazil = pd.read_csv("data/ltbrazil.csv")

# sort the covid data by location and case date in ascending order
coviddaily = coviddaily.sort_values(['location','casedate'])

# iterate over rows with itertuples, append to list with each change of group
prevloc = 'ZZZ'
rowlist = []
for row in coviddaily.itertuples():
  if (prevloc!=row.location):
    if (prevloc!='ZZZ'):
      rowlist.append({'location':prevloc, 'casecnt':casecnt})
    casecnt = 0
    prevloc = row.location
  casecnt += row.new_cases
  
rowlist.append({'location':prevloc, 'casecnt':casecnt})
len(rowlist)
rowlist[0:4]

# create a dataframe from the rowlist
covidtotals = pd.DataFrame(rowlist)
covidtotals.head()

# sort the land temperatures data and drop rows with missing values for temperature
ltbrazil = ltbrazil.sort_values(['station','month'])
ltbrazil = ltbrazil.dropna(subset=['temperature'])

# iterate over rows with itertuples, append to list with each change of group
prevstation = 'ZZZ'
prevtemp = 0
rowlist = []
for row in ltbrazil.itertuples():
  if (prevstation!=row.station):
    if (prevstation!='ZZZ'):
      rowlist.append({'station':prevstation, 'avgtemp':tempcnt/stationcnt, 'stationcnt':stationcnt})
    tempcnt = 0
    stationcnt = 0
    prevstation = row.station

  # choose only rows that are within 3 degrees of the previous temperature  
  if ((0 <= abs(row.temperature-prevtemp) <= 3) or (stationcnt==0)):
    tempcnt += row.temperature
    stationcnt += 1
  
  prevtemp = row.temperature

rowlist.append({'station':prevstation, 'avgtemp':tempcnt/stationcnt, 'stationcnt':stationcnt})
rowlist[0:5]
ltbrazilavgs = pd.DataFrame(rowlist)
ltbrazilavgs.head()


