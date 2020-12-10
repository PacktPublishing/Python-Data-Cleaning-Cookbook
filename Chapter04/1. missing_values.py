# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.0f}'.format
covidtotals = pd.read_csv("data/covidtotalswithmissings.csv")
covidtotals.set_index("iso_code", inplace=True)

# set up the cumulative and demographic columns
totvars = ['location','total_cases','total_deaths','total_cases_pm',
  'total_deaths_pm']
demovars = ['population','pop_density','median_age','gdp_per_capita',
  'hosp_beds']

# check the demographic columns for missing
covidtotals[demovars].isnull().sum(axis=0)
demovarsmisscnt = covidtotals[demovars].isnull().sum(axis=1)
demovarsmisscnt.value_counts()
covidtotals.loc[demovarsmisscnt>=3, ['location'] + demovars].head(5).T
type(demovarsmisscnt)

# check the cumulative columns for missing
covidtotals[totvars].isnull().sum(axis=0)
totvarsmisscnt = covidtotals[totvars].isnull().sum(axis=1)
totvarsmisscnt.value_counts()
covidtotals.loc[totvarsmisscnt>0].T

# use the fillna method to fix the mixing case data
covidtotals.total_cases_pm.fillna(covidtotals.total_cases/
  (covidtotals.population/1000000), inplace=True)
covidtotals.total_deaths_pm.fillna(covidtotals.total_deaths/
  (covidtotals.population/1000000), inplace=True)
covidtotals[totvars].isnull().sum(axis=0)

