# import pandas, numpy
import pandas as pd
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97.csv")
nls97.set_index("personid", inplace=True)
nls97.loc[:, nls97.dtypes == 'object'] = \
  nls97.select_dtypes(['object']). \
  apply(lambda x: x.astype('category'))

# show the names of columns with category data type and check for number of missings
catcols = nls97.select_dtypes(include=["category"]).columns
nls97[catcols].isnull().sum()

# show frequencies for marital status
nls97.maritalstatus.value_counts()

# turn off sorting by frequency
nls97.maritalstatus.value_counts(sort=False)

# show percentages instead of counts
nls97.maritalstatus.value_counts(sort=False, normalize=True)

# do percentages for all government responsibility variables
nls97.filter(like="gov").apply(pd.value_counts, normalize=True)

# do percentages for all government responsibility variables for people who are married
nls97[nls97.maritalstatus=="Married"].\
filter(like="gov").\
apply(pd.value_counts, normalize=True)

# do frequencies and percentages for all category variables in data frame
freqout = open('views/frequencies.txt', 'w') 
for col in nls97.select_dtypes(include=["category"]):
  print(col, "----------------------", "frequencies",
  nls97[col].value_counts(sort=False),"percentages",
  nls97[col].value_counts(normalize=True, sort=False),
  sep="\n\n", end="\n\n\n", file=freqout)

freqout.close()
