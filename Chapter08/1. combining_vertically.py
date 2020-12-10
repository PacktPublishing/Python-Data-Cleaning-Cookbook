# import pandas and numpy
import pandas as pd
import numpy as np
import os
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 50)
pd.options.display.float_format = '{:,.0f}'.format

# load the data for Cameroon and Poland
ltcameroon = pd.read_csv("data/ltcountry/ltcameroon.csv")
ltpoland = pd.read_csv("data/ltcountry/ltpoland.csv")

# concatenate the Cameroon and Poland data
ltcameroon.shape
ltpoland.shape
ltall = pd.concat([ltcameroon, ltpoland])
ltall.country.value_counts()

# concatenate all of the data files
directory = "data/ltcountry"
ltall = pd.DataFrame()
for filename in os.listdir(directory):
  if filename.endswith(".csv"): 
    fileloc = os.path.join(directory, filename)

    # open the next file
    with open(fileloc) as f:
      ltnew = pd.read_csv(fileloc)
      print(filename + " has " + str(ltnew.shape[0]) + " rows.")
      ltall = pd.concat([ltall, ltnew])

      # check for differences in columns
      columndiff = ltall.columns.symmetric_difference(ltnew.columns)
      if (not columndiff.empty):
        print("", "Different column names for:", filename,\
          columndiff, "", sep="\n")


ltall[['country','station','month','temperature','latitude']].sample(5, random_state=1)

# check values in the concatenated data
ltall.country.value_counts().sort_index()
ltall.groupby(['country']).agg({'temperature':['min','mean',\
  'max','count'],'latabs':['min','mean','max','count']})

# fix missing values
ltall['latabs'] = np.where(ltall.country=="Oman", ltall.latitude, ltall.latabs)
ltall.groupby(['country']).agg({'temperature':['min','mean',\
  'max','count'],'latabs':['min','mean','max','count']})
