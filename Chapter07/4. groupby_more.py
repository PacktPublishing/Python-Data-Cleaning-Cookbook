# import pandas, load the nls97 feather file
import pandas as pd
pd.set_option('display.width', 90)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 30)
pd.options.display.float_format = '{:,.1f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)

# review the structure of the nls97 data
nls97.iloc[:,0:7].info()

# look again at some of the data
catvars = ['gender','maritalstatus','highestdegree']

for col in catvars:
  print(col, nls97[col].value_counts().sort_index(), sep="\n\n", end="\n\n\n")


# review some descriptive statistics
contvars = ['satmath','satverbal','weeksworked06','gpaoverall',
  'childathome']

nls97[contvars].describe()

# look at sat math scores by gender
nls97.groupby('gender')['satmath'].mean()

# look at sat math scores by gender and highest degree earned
nls97.groupby(['gender','highestdegree'])['satmath'].mean()

# look at sat math and verbal scores by gender and highest degree earned
nls97.groupby(['gender','highestdegree'])[['satmath','satverbal']].mean()

# add max and standard deviations
nls97.groupby(['gender','highestdegree'])['gpaoverall'].agg(['count','mean','max','std'])

# use a dictionary for more complicated aggregations
pd.options.display.float_format = '{:,.1f}'.format
aggdict = {'weeksworked06':['count', 'mean', 'max','std'], 'childathome':['count', 'mean', 'max', 'std']}
nls97.groupby(['highestdegree']).agg(aggdict)
nls97.groupby(['maritalstatus']).agg(aggdict)
