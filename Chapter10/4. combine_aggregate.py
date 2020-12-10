# import the pandas, os, and sys libraries
import pandas as pd
import os
import sys

# import combineagg module
sys.path.append(os.getcwd() + "/helperfunctions")
import combineagg as ca
# import importlib
# importlib.reload(ca)
pd.set_option('display.width', 150)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 20)

# load the data frames
coviddaily = pd.read_csv("data/coviddaily720.csv")
ltbrazil = pd.read_csv("data/ltbrazil.csv")
countries = pd.read_csv("data/ltcountries.csv")
locations = pd.read_csv("data/ltlocations.csv")

# summarize panel data by group and time period, with exclusions
ca.adjmeans(coviddaily, 'location','new_cases','casedate')
ca.adjmeans(coviddaily, 'location','new_cases','casedate', 150)

# check matches of merge-by values across data frames
ca.checkmerge(countries.copy(), locations.copy(),\
  "countryid", "countryid")

# concatenate all pickle files in a folder, assuming they have the same structure
landtemps = ca.addfiles("data/ltcountry")
landtemps.country.value_counts()
