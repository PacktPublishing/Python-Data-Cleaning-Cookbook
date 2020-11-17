# import the pandas, os, and sys libraries
import pandas as pd
import os
import sys

# import combineagg module
sys.path.append(os.getcwd() + "/helperfunctions")
import combineagg as ca
# import importlib
importlib.reload(ca)
pd.set_option('display.width', 150)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 20)

# load the data frames
coviddaily = pd.read_pickle("data/coviddaily720.pkl")
ltbrazil = pd.read_pickle("data/ltbrazil.pkl")
countries = pd.read_pickle("data/ltcountries.pkl")
locations = pd.read_pickle("data/ltlocations.pkl")

# summarize panel data by group and time period, with exclusions
ca.adjmeans(coviddaily, 'location','new_cases','casedate')
ca.adjmeans(coviddaily, 'location','new_cases','casedate', 150)

# check matches of merge-by values across data frames
ca.checkmerge(countries.copy(), locations.copy(),\
  "countryid", "countryid")

# concatenate all pickle files in a folder, assuming they have the same structure
landtemps = ca.addfiles("data/ltcountry")
landtemps.country.value_counts()

ltoman = pd.read_pickle("data/ltcountry/ltoman.pkl")
landtemps.columns.symmetric_difference(ltoman.columns).empty
not temp.empty