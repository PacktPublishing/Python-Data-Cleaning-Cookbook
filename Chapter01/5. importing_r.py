# import pandas, numpy, and pyreadr
import pandas as pd
import numpy as np
import pyreadr
import pprint
pd.set_option('display.width', 72)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 25)

# get the R data
nls97r = pyreadr.read_r('data/nls97.rds')[None]
nls97r.dtypes
nls97r.head(10)

# load the value labels
with open('data/nlscodes.txt', 'r') as reader:
    setvalues = eval(reader.read())

pprint.pprint(setvalues)

newcols = ['personid','gender','birthmonth','birthyear',
  'sampletype',  'category','satverbal','satmath',
  'gpaoverall','gpaeng','gpamath','gpascience','govjobs',
  'govprices','govhealth','goveld','govind','govunemp',
  'govinc','govcollege','govhousing','govenvironment',
  'bacredits','coltype1','coltype2','coltype3','coltype4',
  'coltype5','coltype6','highestgrade','maritalstatus',
  'childnumhome','childnumaway','degreecol1',
  'degreecol2','degreecol3','degreecol4','wageincome',
  'weeklyhrscomputer','weeklyhrstv',
  'nightlyhrssleep','weeksworkedlastyear']

# set value labels, missing values, and change data type to category
nls97r.replace(setvalues, inplace=True)
nls97r.head()
nls97r.replace(list(range(-9,0)), np.nan, inplace=True)
for col in nls97r[[k for k in setvalues]].columns:
    nls97r[col] = nls97r[col].astype('category')

nls97r.dtypes

# set meaningful column headings and set category data types
nls97r.columns = newcols
nls97r.head()