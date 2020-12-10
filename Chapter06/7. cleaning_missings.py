# import pandas
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 12)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.0f}'.format
nls97 = pd.read_csv("data/nls97c.csv")
nls97.set_index("personid", inplace=True)

# set up school record and demographic data frames from the NLS data
schoolrecordlist = ['satverbal','satmath','gpaoverall','gpaenglish',
  'gpamath','gpascience','highestdegree','highestgradecompleted']

demolist = ['maritalstatus','childathome','childnotathome',
  'wageincome','weeklyhrscomputer','weeklyhrstv','nightlyhrssleep']
schoolrecord = nls97[schoolrecordlist]

demo = nls97[demolist]
schoolrecord.shape
demo.shape

# check the school record data for missings
schoolrecord.isnull().sum(axis=0)
misscnt = schoolrecord.isnull().sum(axis=1)
misscnt.value_counts().sort_index()
schoolrecord.loc[misscnt>=7].head(4).T

# remove rows with almost all missing data
schoolrecord = schoolrecord.dropna(thresh=2)
schoolrecord.shape
schoolrecord.isnull().sum(axis=1).value_counts().sort_index()

# assign mean values to missings
schoolrecord.gpaoverall.mean()
schoolrecord.gpaoverall.isnull().sum()
schoolrecord.gpaoverall.\
  fillna(schoolrecord.gpaoverall.\
  mean(), inplace=True)
schoolrecord.gpaoverall.isnull().sum()

# use forward fill
demo.wageincome.head().T
demo.wageincome.isnull().sum()
nls97.wageincome.fillna(method='ffill', inplace=True)
demo = nls97[demolist]
demo.wageincome.head().T
demo.wageincome.isnull().sum()

# fill missings with the average by group
nls97[['highestdegree','weeksworked17']].head()
workbydegree = nls97.groupby(['highestdegree'])['weeksworked17'].mean().\
  reset_index().rename(columns={'weeksworked17':'meanweeksworked17'})
nls97 = nls97.reset_index().\
  merge(workbydegree, left_on=['highestdegree'], right_on=['highestdegree'], how='left').set_index('personid')
nls97.weeksworked17.fillna(nls97.meanweeksworked17, inplace=True)
nls97[['highestdegree','weeksworked17','meanweeksworked17']].head()
