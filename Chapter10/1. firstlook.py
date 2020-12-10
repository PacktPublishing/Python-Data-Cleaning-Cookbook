# import pandas and os and sys libraries
import pandas as pd
import os
import sys
nls97 = pd.read_csv("data/nls97f.csv")
nls97.set_index('personid', inplace=True)

# import the basicdescriptives module
sys.path.append(os.getcwd() + "/helperfunctions")
import basicdescriptives as bd
# import importlib
# importlib.reload(bd)
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 15)

# take a first look at the NLS data
dfinfo = bd.getfirstlook(nls97)
bd.displaydict(dfinfo)

# pass values to the nrows and uniqueid parameters
dfinfo = bd.getfirstlook(nls97,2,'originalid')
bd.displaydict(dfinfo)

# work with some of the dictionary keys and values
dfinfo['nrows']
dfinfo['dtypes']
dfinfo['nrows'] == dfinfo['uniqueids']

