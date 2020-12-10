# import pandas
import pandas as pd
import numpy as np
from datetime import datetime
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 220)
pd.options.display.float_format = '{:,.0f}'.format
covidcases = pd.read_csv("data/covidcases720.csv")
nls97 = pd.read_csv("data/nls97c.csv")
nls97.set_index("personid", inplace=True)

# show the birth month and year values
nls97[['birthmonth','birthyear']].head()
nls97[['birthmonth','birthyear']].isnull().sum()
nls97.birthmonth.value_counts().sort_index()
nls97.birthyear.value_counts().sort_index()

# use fillna to fix missing value
nls97.birthmonth.fillna(int(nls97.birthmonth.mean()), inplace=True)
nls97.birthmonth.value_counts().sort_index()

# use month and date integers to create a datetime column
nls97['birthdate'] = pd.to_datetime(dict(year=nls97.birthyear, month=nls97.birthmonth, day=15))
nls97.birthdate.describe()
nls97[['birthmonth','birthyear','birthdate']].head()
nls97[['birthmonth','birthyear','birthdate']].isnull().sum()

# define a function for calculating given start and end date
def calcage(startdate, enddate):
  age = enddate.year - startdate.year
  if (enddate.month<startdate.month or (enddate.month==startdate.month and enddate.day<startdate.day)):
    age = age -1
  return age

# calculate age
rundate = pd.to_datetime('2020-07-20')
nls97["age"] = nls97.apply(lambda x: calcage(x.birthdate, rundate), axis=1)
nls97.loc[100061:100583, ['age','birthdate']]

# convert a string column to a datetime column
covidcases.iloc[:, 0:6].dtypes
covidcases.iloc[:, 0:6].sample(2, random_state=1).T
covidcases['casedate'] = pd.to_datetime(covidcases.casedate, format='%Y-%m-%d')
covidcases.iloc[:, 0:6].dtypes

# get descriptive statistics on datetime column
covidcases.casedate.describe()

# calculate days since first case by country
firstcase = covidcases.loc[covidcases.new_cases>0,['location','casedate']].\
  sort_values(['location','casedate']).\
  drop_duplicates(['location'], keep='first').\
  rename(columns={'casedate':'firstcasedate'})
covidcases = pd.merge(covidcases, firstcase, left_on=['location'], right_on=['location'], how="left")
covidcases['dayssincefirstcase'] = covidcases.casedate - covidcases.firstcasedate
covidcases.dayssincefirstcase.describe()





