# import pandas
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.width', 200)

# import the land temperature data
landtemps = pd.read_csv('data/landtemps.zip', compression='zip',
    names=['stationid','year','month','avgtemp','latitude',
      'longitude','elevation','station','countryid','country'],
    skiprows=1,
    parse_dates=[['month','year']],
    low_memory=False)

type(landtemps)

# show enough data to get a sense of how the import went
landtemps.head(7)
landtemps.sample(7)
landtemps.dtypes
landtemps.shape
landtemps[['avgtemp']].describe()

# remove rows with missing values
landtemps.dropna(subset=['avgtemp'], inplace=True)
landtemps.head(7)
landtemps.shape

