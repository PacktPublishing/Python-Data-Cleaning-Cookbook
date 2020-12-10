# import pandas and load the covid data and land temperature data
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 50)
pd.options.display.float_format = '{:,.0f}'.format
coviddaily = pd.read_csv("data/coviddaily720.csv", parse_dates=["casedate"])
ltbrazil = pd.read_csv("data/ltbrazil.csv")

# convert covid data from one country per day to summary values across all countries per day
coviddailytotals = coviddaily.loc[coviddaily.casedate.between('2020-02-01','2020-07-12')].\
  groupby(['casedate'], as_index=False)[['new_cases','new_deaths']].\
  sum()

coviddailytotals.head(10)

# create a data frame with average temperatures from each station in Brazil
ltbrazil = ltbrazil.dropna(subset=['temperature'])
ltbrazil.loc[103508:104551, ['station','year','month','temperature','elevation','latabs']]
ltbrazilavgs = ltbrazil.groupby(['station'], as_index=False).\
  agg({'latabs':'first','elevation':'first','temperature':'mean'})
ltbrazilavgs.head(10)

