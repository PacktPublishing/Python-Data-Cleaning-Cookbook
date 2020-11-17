# import pandas and numpy
import pandas as pd
import numpy as np
import os
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 50)
pd.options.display.float_format = '{:,.0f}'.format

# load the data for Cameroon and Poland
ltcameroon = pd.read_pickle("data/ltcountry/ltcameroon.pkl")
ltpoland = pd.read_pickle("data/ltcountry/ltpoland.pkl")

# concatenate the Cameroon and Poland data
ltcameroon.shape
ltpoland.shape
ltcameroon.shape[0]
ltall = pd.concat([ltcameroon, ltpoland])
ltall.country.value_counts()

# concatenate all of the data files
directory = "data/ltcountry"
ltall = pd.DataFrame()
for filename in os.listdir(directory):
  if filename.endswith(".pkl"): 
    fileloc = os.path.join(directory, filename)

    # open the next file
    with open(fileloc) as f:
      ltnew = pd.read_pickle(fileloc)
      print(filename + " has " + str(ltnew.shape[0]) + " rows.")
      ltall = pd.concat([ltall, ltnew])

      # check for differences in columns
      columndiff = ltall.columns.symmetric_difference(ltnew.columns)
      if (not columndiff.empty):
        print("", "Different column names for:", filename,\
          columndiff, "", sep="\n")


ltall[['country','station','month','temperature','latitude']].head()

# check values in the concatenated data
ltall.country.value_counts().sort_index()
ltall.groupby(['country']).agg({'temperature':['min','mean',\
  'max','count'],'latabs':['min','mean','max','count']})

# fix missing values
ltall['latabs'] = np.where(ltall.country=="Oman", ltall.latitude, ltall.latabs)
ltall.groupby(['country']).agg({'temperature':['min','mean',\
  'max','count'],'latabs':['min','mean','max','count']})
