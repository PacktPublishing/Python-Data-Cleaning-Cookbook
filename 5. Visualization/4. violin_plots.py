# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format
covidtotals = pd.read_pickle("data/covidtotals720.pkl")
nls97 = pd.read_pickle("data/nls97.pkl")

# do a violin plot of sat verbal scores
sns.violinplot(nls97.satverbal, color="wheat", orient="v")
plt.title("Violin Plot of SAT Verbal Score")
plt.ylabel("SAT Verbal")
plt.text(0.08, 780, "outlier threshold", horizontalalignment='center', size='x-small')
plt.text(0.065, nls97.satverbal.quantile(0.75), "3rd quartile",\ horizontalalignment='center', size='x-small')
plt.text(0.05, nls97.satverbal.median(), "Median", horizontalalignment='center', size='x-small')
plt.text(0.065, nls97.satverbal.quantile(0.25), "1st quartile", horizontalalignment='center', size='x-small')
plt.text(0.08, 210, "outlier threshold", horizontalalignment='center', size='x-small')
plt.text(-0.4, 500, "frequency", horizontalalignment='center', size='x-small')
plt.show()

# get some descriptives
nls97.loc[:, ['weeksworked16','weeksworked17','wageincome']].describe()
nls97.wageincome.quantile([0.98,0.99])

# show weeks worked for 2016 and 2017
myplt = sns.violinplot(data=nls97.loc[:, ['weeksworked16','weeksworked17']])
myplt.set_title("Violin Plots of Weeks Worked")
myplt.set_xticklabels(["Weeks Worked 2016","Weeks Worked 2017"])
plt.show()

# do a violin plot of wage income by gender
nls97["maritalstatuscollapsed"] = nls97.maritalstatus.\
  replace(['Married','Never-married','Divorced','Separated','Widowed'],\
  ['Married','Never Married','Not Married','Not Married','Not Married']) 
sns.violinplot(nls97.gender, nls97.wageincome, hue=nls97.maritalstatuscollapsed, scale="count")
plt.title("Violin Plots of Wage Income by Gender and Marital Status")
plt.xlabel('Gender')
plt.ylabel('Wage Income 2017')
plt.legend(title="", loc="upper center", framealpha=0, fontsize=8)
plt.tight_layout()
plt.show()

# do a violin plot of weeks worked by degree attainment
myplt = sns.violinplot('highestdegree','weeksworked17', data=nls97)
myplt.set_xticklabels(myplt.get_xticklabels(), rotation=60, horizontalalignment='right')
myplt.set_title("Violin Plots of Weeks Worked by Highest Degree")
myplt.set_xlabel('Highest Degree Attained')
myplt.set_ylabel('Weeks Worked 2017')
plt.tight_layout()
plt.show()

# do a violin plot of covid cases by selected regions
showregions = ['Oceania / Aus','East Asia','Africa (other)','Western Europe']
covidselect = covidtotals.loc[covidtotals.region.isin(showregions)]
sns.violinplot('region', 'total_cases_pm', order=showregions, data=covidselect)
sns.swarmplot(x="region", y="total_cases_pm", order=showregions,\
  data=covidselect, size=3, color=".3", linewidth=0)
plt.title("Violin Plot of Total Cases Per Million by Region")
plt.xlabel("Cases Per Million")
plt.ylabel("Region")
plt.tight_layout()
plt.show()

# use matplotlib for violin plot
plt.violinplot(nls97.satverbal.dropna(), showmedians=True, quantiles=[0.05, 0.1, 0.8, 0.9], bw_method=0.5)
plt.title("Violin Plot of SAT Verbal Score")
plt.show()

myplt = sns.violinplot(data=nls97.loc[:, ['weeksworked16','weeksworked17']])
myplt.set_title("Violin Plots of Weeks Worked")
myplt.set_xticklabels(["Weeks Worked 2016","Weeks Worked 2017"])
plt.show()

