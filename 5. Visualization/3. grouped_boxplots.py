# import pandas, matplotlib, and seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format
nls97 = pd.read_pickle("data/nls97.pkl")
covidtotals = pd.read_pickle("data/covidtotals720.pkl")



def gettots(x):
  out = {}
  out['min'] = x.min()
  out['qr1'] = x.quantile(0.25)
  out['med'] = x.median()
  out['qr3'] = x.quantile(0.75)
  out['max'] = x.max()
  out['count'] = x.count()
  return pd.Series(out)

nls97.groupby(['highestdegree'])['weeksworked17'].\
  apply(gettots).unstack()

# do boxplots for weeks worked by highest degree earned
myplt = sns.boxplot('highestdegree','weeksworked17', data=nls97)
myplt.set_title("Boxplots of Weeks Worked by Highest Degree")
myplt.set_xlabel('Highest Degree Attained')
myplt.set_ylabel('Weeks Worked 2017')
myplt.set_xticklabels(myplt.get_xticklabels(), rotation=60, horizontalalignment='right')
plt.tight_layout()
plt.show()


covidtotals.groupby(['region'])['total_cases_pm'].\
  apply(gettots).unstack()

# do boxplots for cases per million by region
sns.boxplot('total_cases_pm', 'region', data=covidtotals)
sns.swarmplot(y="region", x="total_cases_pm", data=covidtotals, size=2, color=".3", linewidth=0)
plt.title("Boxplots of Total Cases Per Million by Region")
plt.xlabel("Cases Per Million")
plt.ylabel("Region")
plt.tight_layout()
plt.show()

# show the most extreme value for covid totals
covidtotals.loc[covidtotals.total_cases_pm>=14000,\
  ['location','total_cases_pm']]

# do the same boxplots without the one extreme value in West Asia
sns.boxplot('total_cases_pm', 'region', data=covidtotals.loc[covidtotals.total_cases_pm<14000])
sns.swarmplot(y="region", x="total_cases_pm", data=covidtotals.loc[covidtotals.total_cases_pm<14000], size=3, color=".3", linewidth=0)
plt.title("Total Cases Without Extreme Values")
plt.xlabel("Cases Per Million")
plt.ylabel("Region")
plt.tight_layout()
plt.show()

