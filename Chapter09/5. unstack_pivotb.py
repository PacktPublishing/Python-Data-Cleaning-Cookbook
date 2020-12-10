# import pandas and load the stacked and melted nls data
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format
nls97 = pd.read_csv("data/nls97f.csv")
nls97.set_index(['originalid'], inplace=True)

# stack the data again
weeksworkedcols = ['weeksworked00','weeksworked01',
  'weeksworked02','weeksworked03','weeksworked04']

weeksworkedstacked = nls97[weeksworkedcols].\
  stack(dropna=False)
weeksworkedstacked.loc[[1,2]]

# melt the data again
weeksworkedmelted = nls97.reset_index().\
  loc[:,['originalid'] + weeksworkedcols].\
  melt(id_vars=['originalid'], value_vars=weeksworkedcols,
    var_name='year', value_name='weeksworked')
weeksworkedmelted.loc[weeksworkedmelted.originalid.isin([1,2])].\
  sort_values(['originalid','year'])

# use stack to convert from long to wide
weeksworked = weeksworkedstacked.unstack()
weeksworked.loc[[1,2]]

# use pivot to convert from long to wide
weeksworked = weeksworkedmelted.pivot(index='originalid', \
  columns='year', values=['weeksworked']).reset_index()
weeksworked.columns = ['originalid'] + \
  [col[1] for col in weeksworked.columns[1:]]
weeksworked.loc[weeksworked.originalid.isin([1,2])].T

