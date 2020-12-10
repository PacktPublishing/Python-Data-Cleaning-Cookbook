# import pandas, matplotlib, and statsmodels
import pandas as pd
import numpy as np
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)

# show some descriptive statistics
gpaoverall = nls97.gpaoverall
gpaoverall.mean()
gpaoverall.describe()
gpaoverall.quantile(np.arange(0.1,1.1,0.1))

# subset based on values
gpaoverall.loc[gpaoverall.between(3,3.5)].head(5)
gpaoverall.loc[gpaoverall.between(3,3.5)].count()
gpaoverall.loc[(gpaoverall<2) | (gpaoverall>4)].sample(5, random_state=2)
gpaoverall.loc[gpaoverall>gpaoverall.quantile(0.99)].\
  agg(['count','min','max'])

# run tests across all values
(gpaoverall>4).any() # any person has GPA greater than 4
(gpaoverall>=0).all() # all people have GPA greater than 0
(gpaoverall>=0).sum() # of people with GPA greater than 0
(gpaoverall==0).sum() # of people with GPA equal to 0
gpaoverall.isnull().sum() # of people with missing value for GPA

# show GPA for high and low wage income earners
nls97.loc[nls97.wageincome > nls97.wageincome.quantile(0.75),'gpaoverall'].mean()
nls97.loc[nls97.wageincome < nls97.wageincome.quantile(0.25),'gpaoverall'].mean()

# show counts for series with categorical data
nls97.maritalstatus.describe()
nls97.maritalstatus.value_counts()
