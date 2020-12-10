# import pandas, matplotlib, and statsmodels
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)

# multiply all values of a series by a scalar
nls97.gpaoverall.head()
gpaoverall100 = nls97['gpaoverall'] * 100
gpaoverall100.head()

# use loc accessor to apply a scalar to selected rows
nls97.loc[[100061], 'gpaoverall'] = 3
nls97.loc[[100139,100284,100292],'gpaoverall'] = 0
nls97.gpaoverall.head()

# set values using more than one series
nls97['childnum'] = nls97.childathome + nls97.childnotathome
nls97.childnum.value_counts().sort_index()

# use indexing to apply a summary value to selected rows
nls97.loc[100061:100292,'gpaoverall'] = nls97.gpaoverall.mean()
nls97.gpaoverall.head()

# use iloc accessor to apply a scalar to selected rows
nls97.iloc[0, 13] = 2
nls97.iloc[1:4, 13] = 1
nls97.gpaoverall.head()

# set values after filtering
nls97.gpaoverall.nlargest()
nls97.loc[nls97.gpaoverall>4, 'gpaoverall'] = 4
nls97.gpaoverall.nlargest()

type(nls97.loc[[100061], 'gpaoverall'])
type(nls97.loc[[100061], ['gpaoverall']])
