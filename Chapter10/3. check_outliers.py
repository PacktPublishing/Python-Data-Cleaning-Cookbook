# import the pandas, os, and sys libraries and load the nls and covid data
import pandas as pd
import os
import sys
import pprint
nls97 = pd.read_csv("data/nls97f.csv")
nls97.set_index('personid', inplace=True)
covidtotals = pd.read_csv("data/covidtotals720.csv")

# import the outliers module
sys.path.append(os.getcwd() + "/helperfunctions")
import outliers as ol
# import importlib
#importlib.reload(ol)
pd.set_option('display.width', 72)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 100)

# get the distribution of a variable
dist = ol.getdistprops(covidtotals.total_cases_pm)
pprint.pprint(dist)

# show outlier rows
sumvars = ['satmath','wageincome']
othervars = ['originalid','highestdegree','gender','maritalstatus']
outliers = ol.getoutliers(nls97, sumvars, othervars)
outliers.varname.value_counts(sort=False)
outliers.loc[outliers.varname=='satmath', othervars + sumvars]
outliers.to_excel("views/nlsoutliers.xlsx")

# do histogram or boxplot of a series
ol.makeplot(nls97.satmath, "Histogram of SAT Math", "SAT Math")
ol.makeplot(nls97.satmath, "Boxplot of SAT Math", "SAT Math", "box")

