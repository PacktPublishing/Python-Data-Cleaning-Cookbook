# import pandas and load the stacked and melted nls data
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format
weeksworkedstacked = pd.read_pickle("data/nlsweeksworkedstacked.pkl")
workschoolmelted = pd.read_pickle("data/nlsworkschoolmelted.pkl")

# view the stacked weeks worked data
weeksworkedstacked.head(10)
weeksworkedstacked.index

# use stack to convert from long to wide
weeksworked = weeksworkedstacked.unstack()
weeksworked.head(10)

# use pivot to convert from long to wide
workschoolmelted.loc[workschoolmelted.originalid.isin([1,2])].sort_values(['originalid','year'])
workschool = workschoolmelted.pivot(index='originalid', columns='year', values=['weeksworked','colenroct']).reset_index()
workschool.columns = workschool.columns.map('{0[0]}{0[1]}'.format)
workschool.loc[workschool.originalid.isin([1,2])].T

