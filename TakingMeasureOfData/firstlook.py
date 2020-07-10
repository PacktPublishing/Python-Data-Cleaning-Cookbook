# import pandas, numpy
import pandas as pd
import numpy as np
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.0f}'.format
nls97 = pd.read_pickle("data/nls97.pkl")
covidtotals = pd.read_pickle("data/covidtotals.pkl")

# Get basic stats on the nls dataset
nls97.index
nls97.shape
nls97.info()
nls97.head(2).T

# Get basic stats on the covid cases dataset
covidtotals.index
covidtotals.shape
covidtotals.info()
covidtotals.sample(2).T
