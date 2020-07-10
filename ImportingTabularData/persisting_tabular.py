# import pandas and pyarrow
import pandas as pd
import pyarrow
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.width', 68)
pd.set_option('display.max_columns', 3)

# import the land temperature data
landtemps = pd.read_csv('data/landtempssample.csv',
    names=['stationid','year','month','avgtemp','latitude',
      'longitude','elevation','station','countryid','country'],
    skiprows=1,
    parse_dates=[['month','year']],
    low_memory=False)

landtemps.rename(columns={'month_year':'measuredate'}, inplace=True)
landtemps.dropna(subset=['avgtemp'], inplace=True)
landtemps.dtypes
landtemps.set_index(['measuredate','stationid'], inplace=True)

# write extreme values of temperature out to Excel and CSV files
extremevals = landtemps[(landtemps.avgtemp < landtemps.avgtemp.quantile(.001)) | (landtemps.avgtemp > landtemps.avgtemp.quantile(.999))]
extremevals.shape
extremevals.sample(7)
extremevals.to_excel('views/tempext.xlsx')
extremevals.to_csv('views/tempext.csv')

# save to pickle and feather files
landtemps.to_pickle('data/landtemps.pkl')
landtemps.reset_index(inplace=True)
landtemps.to_feather("data/landtemps.ftr")

# load saved pickle and feather files
landtemps = pd.read_pickle('data/landtemps.pkl')
landtemps.head(2).T
landtemps = pd.read_feather("data/landtemps.ftr")
landtemps.head(2).T
