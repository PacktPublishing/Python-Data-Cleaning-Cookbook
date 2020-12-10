# import pandas and numpy, and load the covid data
import pandas as pd
import numpy as np
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 50)
pd.options.display.float_format = '{:,.0f}'.format
coviddaily = pd.read_csv("data/coviddaily720.csv", parse_dates=["casedate"])

# create a pandas groupby data frame
countrytots = coviddaily.groupby(['location'])
type(countrytots)

# create data frames for the first and last rows for each country
countrytots.first().iloc[0:5, 0:5]
countrytots.last().iloc[0:5, 0:5]
type(countrytots.last())

# get all of the rows for a country
countrytots.get_group('Zimbabwe').iloc[0:5, 0:5]

# loop through the groups
for name, group in countrytots:
  if (name in ['Malta','Kuwait']):
    print(group.iloc[0:5, 0:5])

# show the number of rows for each country
countrytots.size()

# show summary statistics by country
countrytots.new_cases.describe().head()
countrytots.new_cases.sum().head()

