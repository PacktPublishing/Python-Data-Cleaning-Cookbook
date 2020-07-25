# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format
coviddaily = pd.read_pickle("data/coviddaily720.pkl")

# look at a couple of sample rows of the covid daily data
coviddaily.sample(2).T

# calculate new cases and deaths by day
coviddailytotals = coviddaily.loc[coviddaily.casedate.between('2020-02-01','2020-07-12')].\
  groupby(['casedate'])[['new_cases','new_deaths']].\
  sum().\
  reset_index()

coviddailytotals.sample(7)

# show line charts for new cases and new deaths by day
fig = plt.figure()
plt.suptitle("New Covid Cases and Deaths By Day Worldwide in 2020")
ax1 = plt.subplot(2,1,1)
ax1.plot(coviddailytotals.casedate, coviddailytotals.new_cases)
ax1.xaxis.set_major_formatter(DateFormatter("%b"))
ax1.set_xlabel("New Cases")
ax2 = plt.subplot(2,1,2)
ax2.plot(coviddailytotals.casedate, coviddailytotals.new_deaths)
ax2.xaxis.set_major_formatter(DateFormatter("%b"))
ax2.set_xlabel("New Deaths")
plt.tight_layout()
fig.subplots_adjust(top=0.88)
plt.show()

# calculate new cases and new deaths by region and day
regiontotals = coviddaily.loc[coviddaily.casedate.between('2020-02-01','2020-07-12')].\
  groupby(['casedate','region'])[['new_cases','new_deaths']].\
  sum().\
  reset_index()
regiontotals.sample(7)

# show plot of new cases by selected regions
ea, we, na, af = regiontotals.loc[regiontotals.region=="East Asia"],\
  regiontotals.loc[regiontotals.region=="Western Europe"],\
  regiontotals.loc[regiontotals.region=="North America"],\
  regiontotals.loc[regiontotals.region=="Africa (other)"]
ax = plt.subplot()
ax.plot(ea.casedate, ea.new_cases, label="East Asia")
ax.plot(we.casedate, we.new_cases, label="Western Europe")
ax.plot(na.casedate, na.new_cases, label="North America")
ax.plot(af.casedate, af.new_cases, label="Africa (other)")
ax.xaxis.set_major_formatter(DateFormatter("%b"))
plt.title("New Covid Cases By Day and Region in 2020")
plt.ylabel("New Cases")
plt.legend()
plt.show()

sa = coviddaily.loc[coviddaily.location=='South Africa',['casedate','new_cases']].rename(columns={'new_cases':'sacases'})
af = af[['casedate','new_cases']].rename(columns={'new_cases':'afcases'})
af = pd.merge(af, sa, left_on=['casedate'], right_on=['casedate'], how="left")
af.sacases.fillna(0, inplace=True)
af['afcasesnosa'] = af.afcases-af.sacases
afabb = af.loc[af.casedate.between('2020-04-01','2020-07-12')]

fig = plt.figure()
ax = plt.subplot()
ax.stackplot(afabb.casedate, afabb.sacases, afabb.afcasesnosa, labels=['South Africa','Other Africa'])
ax.xaxis.set_major_formatter(DateFormatter("%m-%d"))
plt.title("New Covid Cases in Africa")
plt.tight_layout()
plt.legend(loc="upper left")
plt.show()
