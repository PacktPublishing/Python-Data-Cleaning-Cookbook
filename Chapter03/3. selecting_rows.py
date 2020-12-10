# import pandas and numpy, and load the nls97 data
import pandas as pd
import numpy as np
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97.csv")
nls97.set_index("personid", inplace=True)

# use slicing to select a few rows
nls97[1000:1004].T

nls97[1000:1004:2].T

# select first 3 rows using head() and Python slicing
nls97.head(3).T
nls97[:3].T

# select last 3 rows using tail() and Python slicing
nls97.tail(3).T
nls97[-3:].T

# select a few rows using loc and iloc
nls97.loc[[195884,195891,195970]].T
nls97.loc[195884:195970].T
nls97.iloc[[0]].T
nls97.iloc[[0,1,2]].T
nls97.iloc[0:3].T
nls97.iloc[[-3,-2,-1]].T
nls97.iloc[-3:].T

# select multiple rows conditionally
nls97.nightlyhrssleep.quantile(0.05)
nls97.nightlyhrssleep.count()
sleepcheckbool = nls97.nightlyhrssleep<=4
sleepcheckbool
lowsleep = nls97.loc[sleepcheckbool]
lowsleep = nls97.loc[nls97.nightlyhrssleep<=4]
lowsleep.shape

# select rows based on multiple conditions
lowsleep.childathome.describe()
lowsleep3pluschildren = nls97.loc[(nls97.nightlyhrssleep<=4) & (nls97.childathome>=3)]
lowsleep3pluschildren.shape

# select rows based on multiple conditions and also select columns
lowsleep3pluschildren = nls97.loc[(nls97.nightlyhrssleep<=4) & (nls97.childathome>=3), ['nightlyhrssleep','childathome']]
lowsleep3pluschildren
