# import pandas and numpy, and load the nls and land temperatures data
import pandas as pd
import numpy as np
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)
landtemps = pd.read_csv("data/landtemps2019avgs.csv")

# use the numpy where function to create a categorical series with 2 values

landtemps.elevation.quantile(np.arange(0.2,1.1,0.2))

landtemps['elevation_group'] = np.where(landtemps.elevation>\
  landtemps.elevation.quantile(0.8),'High','Low')
landtemps.elevation_group = landtemps.elevation_group.astype('category')
landtemps.groupby(['elevation_group'])['elevation'].agg(['count','min','max'])

# use the numpy where function to create a categorical series with 3 values
landtemps.elevation.median()
landtemps['elevation_group'] = np.where(landtemps.elevation>
  landtemps.elevation.quantile(0.8),'High',np.where(landtemps.elevation>
  landtemps.elevation.median(),'Medium','Low'))
landtemps.elevation_group = landtemps.elevation_group.astype('category')
landtemps.groupby(['elevation_group'])['elevation'].agg(['count','min','max'])

# use numpy select to evaluate a list of conditions
test = [(nls97.gpaoverall<2) & (nls97.highestdegree=='0. None'), nls97.highestdegree=='0. None', nls97.gpaoverall<2]
result = ['1. Low GPA and No Diploma','2. No Diploma','3. Low GPA']
nls97['hsachieve'] = np.select(test, result, '4. Did Okay')
nls97[['hsachieve','gpaoverall','highestdegree']].head()
nls97.hsachieve.value_counts().sort_index()

# create a flag if individual ever had bachelor degree enrollment
nls97.loc[[100292,100583,100139], 'colenrfeb00':'colenroct04'].T
nls97['baenrollment'] = nls97.filter(like="colenr").\
  apply(lambda x: x.str[0:1]=='3').\
  any(axis=1)

nls97.loc[[100292,100583,100139], ['baenrollment']].T
nls97.baenrollment.value_counts()

# use apply and lambda to create a more complicated categorical series
def getsleepdeprivedreason(row):
  sleepdeprivedreason = "Unknown"
  if (row.nightlyhrssleep>=6):
    sleepdeprivedreason = "Not Sleep Deprived"
  elif (row.nightlyhrssleep>0):
    if (row.weeksworked16+row.weeksworked17 < 80):
      if (row.childathome>2):
        sleepdeprivedreason = "Child Rearing"
      else:
        sleepdeprivedreason = "Other Reasons"
    else:
      if (row.wageincome>=62000 or row.highestgradecompleted>=16):
        sleepdeprivedreason = "Work Pressure"
      else:
        sleepdeprivedreason = "Income Pressure"
  else:
    sleepdeprivedreason = "Unknown"
  return sleepdeprivedreason

nls97['sleepdeprivedreason'] = nls97.apply(getsleepdeprivedreason, axis=1)
nls97.sleepdeprivedreason = nls97.sleepdeprivedreason.astype('category')
nls97.sleepdeprivedreason.value_counts()
