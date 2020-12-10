# import pandas, numpy
import pandas as pd
import numpy as np
pd.set_option('display.width', 70)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.0f}'.format
nls97 = pd.read_csv("data/nls97.csv")
covidtotals = pd.read_csv("data/covidtotals.csv",
  parse_dates=['lastdate'])

# Get basic stats on the nls dataset

nls97.set_index("personid", inplace=True)
nls97.index
nls97.shape
nls97.index.nunique()
nls97.info()
nls97.head(2).T

# Get basic stats on the covid cases dataset
covidtotals.set_index("iso_code", inplace=True)
covidtotals.index
covidtotals.shape
covidtotals.index.nunique()
covidtotals.info()
covidtotals.sample(2, random_state=1).T
