# import pandas and the land temperatures data
import pandas as pd
countries = pd.read_csv("data/ltcountries.csv")
locations = pd.read_csv("data/ltlocations.csv")

# set index for the locations and countries data and print a few rows
countries.set_index(['countryid'], inplace=True)
locations.set_index(['countryid'], inplace=True)
countries.head()
countries.index.nunique()==countries.shape[0]
locations[['locationid','latitude','stnelev']].head(10)

# do a left join of countries to locations 
stations = countries.join(locations)
stations[['locationid','latitude','stnelev','country']].head(10)

# reload the locations file and check the merge
countries = pd.read_csv("data/ltcountries.csv")
locations = pd.read_csv("data/ltlocations.csv")
def checkmerge(dfleft, dfright, idvar):
  dfleft['inleft'] = "Y"
  dfright['inright'] = "Y"
  dfboth = pd.merge(dfleft[[idvar,'inleft']],\
    dfright[[idvar,'inright']], on=[idvar], how="outer")
  dfboth.fillna('N', inplace=True)
  print(pd.crosstab(dfboth.inleft, dfboth.inright))
  print(dfboth.loc[(dfboth.inleft=='N') | (dfboth.inright=='N')])

checkmerge(countries.copy(), locations.copy(), "countryid")

# show rows in one file and not another
countries.loc[countries.countryid.isin(["LQ","ST"])]
locations.loc[locations.countryid=="FO"]

# merge location and country data
stations = pd.merge(countries, locations, on=["countryid"], how="left")
stations[['locationid','latitude','stnelev','country']].head(10)
stations.shape
stations.loc[stations.countryid.isin(["LQ","ST"])].isnull().sum()

