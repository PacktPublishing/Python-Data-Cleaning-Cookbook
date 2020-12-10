# import pandas and load the nls data
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format
nls97 = pd.read_csv("data/nls97f.csv")

# view some of the weeks worked values
nls97.set_index(['originalid'], inplace=True)
weeksworkedcols = ['weeksworked00','weeksworked01','weeksworked02',
  'weeksworked03','weeksworked04']

nls97[weeksworkedcols].head(2).T
nls97.shape

# use stack to convert data from wide to long
weeksworked = nls97[weeksworkedcols].\
  stack(dropna=False).\
  reset_index().\
  rename(columns={'level_1':'year',0:'weeksworked'})

weeksworked.head(10)

# Fix the year values
weeksworked['year'] = weeksworked.year.str[-2:].astype(int)+2000
weeksworked.head(10)
weeksworked.shape

# use melt to transform data from wide to long
weeksworked = nls97.reset_index().\
  loc[:,['originalid'] + weeksworkedcols].\
  melt(id_vars=['originalid'], value_vars=weeksworkedcols,
    var_name='year', value_name='weeksworked')

weeksworked['year'] = weeksworked.year.str[-2:].astype(int)+2000
weeksworked.set_index(['originalid'], inplace=True)
weeksworked.loc[[8245,3962]]

# reshape more columns with melt
colenrcols = ['colenroct00','colenroct01','colenroct02',
  'colenroct03','colenroct04']
colenr = nls97.reset_index().\
  loc[:,['originalid'] + colenrcols].\
  melt(id_vars=['originalid'], value_vars=colenrcols,
    var_name='year', value_name='colenr')

colenr['year'] = colenr.year.str[-2:].astype(int)+2000
colenr.set_index(['originalid'], inplace=True)
colenr.loc[[8245,3962]]

# merge the weeks worked and enrollment data
workschool = pd.merge(weeksworked, colenr, on=['originalid','year'], how="inner")
workschool.shape
workschool.set_index(['originalid'], inplace=True)
workschool.loc[[8245,3962]]
