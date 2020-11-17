# import pandas
import pandas as pd
pd.options.display.float_format = '{:.0f}'.format
pd.set_option('display.width', 85)
pd.set_option('display.max_columns', 5)

# import the land temperature data
percapitaGDP = pd.read_excel("data/GDPpercapita.xlsx",
   sheet_name="OECD.Stat export",
   skiprows=4,
   skipfooter=1,
   usecols="A,C:T")

percapitaGDP.head()
percapitaGDP.info()

# rename the Year column to metro
percapitaGDP.rename(columns={'Year':'metro'}, inplace=True)
percapitaGDP.metro.str.startswith(' ').any()
percapitaGDP.metro.str.endswith(' ').any()
percapitaGDP.metro = percapitaGDP.metro.str.strip()

# convert the data columns to numeric
for col in percapitaGDP.columns[1:]:
  percapitaGDP[col] = pd.to_numeric(percapitaGDP[col], errors='coerce')
  percapitaGDP.rename(columns={col:'pcGDP'+col}, inplace=True)

percapitaGDP.head()
percapitaGDP.dtypes
percapitaGDP.describe()

# remove rows where all of the per capita GDP values are missing
percapitaGDP.dropna(subset=percapitaGDP.columns[1:], how="all", inplace=True)
percapitaGDP.describe()
percapitaGDP.head()
percapitaGDP.shape

# set an index using the metropolitan area column
percapitaGDP.metro.count()
percapitaGDP.metro.nunique()
percapitaGDP.set_index('metro', inplace=True)
percapitaGDP.head()
percapitaGDP.loc['AUS02: Greater Melbourne']
