# import pandas, numpy, matplotlib, statsmodels, and load the covid totals data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
pd.set_option('display.width', 85)
pd.options.display.float_format = '{:,.0f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)

# create an analysis file
xvars = ['pop_density','median_age','gdp_per_capita']

covidanalysis = covidtotals.loc[:,['total_cases_pm'] + xvars].dropna()
covidanalysis.describe()

# fit a linear regression model
def getlm(df):
  Y = df.total_cases_pm
  X = df[['pop_density','median_age','gdp_per_capita']]
  X = sm.add_constant(X)
  return sm.OLS(Y, X).fit()

lm = getlm(covidanalysis)
lm.summary()

# identify countries with an outsized influence on the model
influence = lm.get_influence().summary_frame()
influence.loc[influence.cooks_d>0.5, ['cooks_d']]
covidanalysis.loc[influence.cooks_d>0.5]

# do an influence plot
fig, ax = plt.subplots()
sm.graphics.influence_plot(lm, ax = ax, criterion="cooks")
plt.show()

# show a model without the outliers
covidanalysisminusoutliers = covidanalysis.loc[influence.cooks_d<0.5]

lm = getlm(covidanalysisminusoutliers)
lm.summary()
