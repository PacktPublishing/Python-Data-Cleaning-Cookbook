# import pandas, numpy, and covid cases daily data
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
covidcases = pd.read_csv("data/covidcases720.csv")

# create lists for daily cases, for cumulative columns and for demographic columns
dailyvars = ['casedate','new_cases','new_deaths']
totvars = ['location','total_cases','total_deaths']

demovars = ['population','population_density','median_age',
  'gdp_per_capita','hospital_beds_per_thousand','region']
covidcases[dailyvars + totvars + demovars].head(3).T

# create a daily data frames
coviddaily = covidcases[['location'] + dailyvars]
coviddaily.shape
coviddaily.head()

# select one row per country
covidcases.location.nunique()
coviddemo = covidcases[['casedate'] + totvars + demovars].\
  sort_values(['location','casedate']).\
  drop_duplicates(['location'], keep='last').\
  rename(columns={'casedate':'lastdate'})

coviddemo.shape
coviddemo.head(3).T

# sum values for each group
covidtotals = covidcases.groupby(['location'], as_index=False).\
  agg({'new_cases':'sum','new_deaths':'sum','median_age':'last',
    'gdp_per_capita':'last','region':'last','casedate':'last',
    'population':'last'}).\
  rename(columns={'new_cases':'total_cases',
    'new_deaths':'total_deaths','casedate':'lastdate'})
  
covidtotals.head(3).T
