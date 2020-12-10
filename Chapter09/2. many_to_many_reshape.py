# import pandas and the CMA collections data
import pandas as pd
pd.options.display.float_format = '{:,.0f}'.format
cma = pd.read_csv("data/cmacollections.csv")

# show the cma collections data
cma.shape
cma.head(2).T
cma.id.nunique()
cma.drop_duplicates(['id','citation']).id.count()
cma.drop_duplicates(['id','creator']).id.count()

# show a collection item with duplicated citations and creators
cma.set_index(['id'], inplace=True)
cma.loc[124733, ['title','citation','creator','birth_year']].head(14)

# create a collections data frame
collectionsvars = ['title','collection','type']
cmacollections = cma[collectionsvars].\
  reset_index().\
  drop_duplicates(['id']).\
  set_index(['id'])
cmacollections.shape
cmacollections.head()
cmacollections.loc[124733]

# create a citations data frame
cmacitations = cma[['citation']].\
  reset_index().\
  drop_duplicates(['id','citation']).\
  set_index(['id'])
cmacitations.loc[124733]

# create a creators data frame
creatorsvars = ['creator','birth_year','death_year']
cmacreators = cma[creatorsvars].\
  reset_index().\
  drop_duplicates(['id','creator']).\
  set_index(['id'])
cmacreators.loc[124733]

# count the number of collection items with a creator born after 1950
cmacreators['birth_year'] = cmacreators.birth_year.str.findall("\d+").str[0].astype(float)
youngartists = cmacreators.loc[cmacreators.birth_year>1950, ['creator']].assign(creatorbornafter1950='Y')
youngartists.shape[0]==youngartists.index.nunique()
youngartists
cmacollections = pd.merge(cmacollections, youngartists, left_on=['id'], right_on=['id'], how='left')
cmacollections.creatorbornafter1950.fillna("N", inplace=True)
cmacollections.shape
cmacollections.creatorbornafter1950.value_counts()
