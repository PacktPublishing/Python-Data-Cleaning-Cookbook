# import pandas and numpy, and load the nls97 data
import pandas as pd
import numpy as np
pd.set_option('display.width', 100)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 15)
pd.options.display.float_format = '{:,.0f}'.format
nls97 = pd.read_csv("data/nls97.csv")
nls97.set_index("personid", inplace=True)
nls97.loc[:, nls97.dtypes == 'object'] = \
  nls97.select_dtypes(['object']). \
  apply(lambda x: x.astype('category'))

# select a column using the pandas index operator
analysisdemo = nls97['gender']
type(analysisdemo)
analysisdemo = nls97[['gender']]
type(analysisdemo)
analysisdemo.dtypes
analysisdemo = nls97.loc[:,['gender']]
type(analysisdemo)
analysisdemo.dtypes
analysisdemo = nls97.iloc[:,[0]]
type(analysisdemo)
analysisdemo.dtypes

# select multiple columns from a pandas data frame
analysisdemo = nls97[['gender','maritalstatus',
 'highestgradecompleted']]
analysisdemo.shape
analysisdemo.head()

analysisdemo = nls97.loc[:,['gender','maritalstatus',
 'highestgradecompleted']]
analysisdemo.shape
analysisdemo.head()

# use lists to select multiple columns
keyvars = ['gender','maritalstatus',
 'highestgradecompleted','wageincome',
 'gpaoverall','weeksworked17','colenroct17']
analysiskeys = nls97[keyvars]
analysiskeys.info()

# select multiple columns using the filter operator
analysiswork = nls97.filter(like="weeksworked")
analysiswork.info()

# select multiple columns based on data types
analysiscats = nls97.select_dtypes(include=["category"])
analysiscats.info()

analysisnums = nls97.select_dtypes(include=["number"])
analysisnums.info()

# organize columns
demo = ['gender','birthmonth','birthyear']
highschoolrecord = ['satverbal','satmath','gpaoverall',
 'gpaenglish','gpamath','gpascience']
govresp = ['govprovidejobs','govpricecontrols',
  'govhealthcare','govelderliving','govindhelp',
  'govunemp','govincomediff','govcollegefinance',
  'govdecenthousing','govprotectenvironment']
demoadult = ['highestgradecompleted','maritalstatus',
  'childathome','childnotathome','wageincome',
  'weeklyhrscomputer','weeklyhrstv','nightlyhrssleep',
  'highestdegree']
weeksworked = ['weeksworked00','weeksworked01',
  'weeksworked02','weeksworked03','weeksworked04',
  'weeksworked05','weeksworked06',  'weeksworked07',
  'weeksworked08','weeksworked09','weeksworked10',
  'weeksworked11','weeksworked12','weeksworked13',
  'weeksworked14','weeksworked15','weeksworked16',
  'weeksworked17']
colenr = ['colenrfeb97','colenroct97','colenrfeb98',
  'colenroct98','colenrfeb99',  'colenroct99',
  'colenrfeb00','colenroct00','colenrfeb01',
  'colenroct01','colenrfeb02','colenroct02',
  'colenrfeb03','colenroct03','colenrfeb04',
  'colenroct04','colenrfeb05','colenroct05',
  'colenrfeb06','colenroct06','colenrfeb07',
  'colenroct07','colenrfeb08','colenroct08',
  'colenrfeb09','colenroct09','colenrfeb10',
  'colenroct10','colenrfeb11','colenroct11',
  'colenrfeb12','colenroct12','colenrfeb13',
  'colenroct13',  'colenrfeb14','colenroct14',
  'colenrfeb15','colenroct15','colenrfeb16',
  'colenroct16','colenrfeb17','colenroct17']

nls97 = nls97[demoadult + demo + highschoolrecord + \
  govresp + weeksworked + colenr]
nls97.dtypes

nls97.select_dtypes(exclude=["category"]).info()

nls97.filter(regex='income')

