# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.2f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv",
  parse_dates=['lastdate'])
covidtotals.set_index("iso_code", inplace=True)

# look at a few rows of the covid cases data
covidtotals.shape
covidtotals.sample(2, random_state=1).T
covidtotals.dtypes

# get descriptive statistics on the cumulative values
covidtotals.describe()
totvars = ['location','total_cases','total_deaths',
  'total_cases_pm','total_deaths_pm']
covidtotals[totvars].quantile(np.arange(0.0, 1.1, 0.1))

# view the distribution of total cases
plt.hist(covidtotals['total_cases']/1000, bins=12)
plt.title("Total Covid Cases (in thousands)")
plt.xlabel('Cases')
plt.ylabel("Number of Countries")
plt.show()
