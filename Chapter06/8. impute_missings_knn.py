# import pandas and scikit learn's KNNImputer module
import pandas as pd
from sklearn.impute import KNNImputer
pd.options.display.float_format = '{:,.1f}'.format
nls97 = pd.read_csv("data/nls97c.csv")
nls97.set_index("personid", inplace=True)

# load the NLS school record data
schoolrecordlist = ['satverbal','satmath','gpaoverall','gpaenglish',
  'gpamath','gpascience','highestgradecompleted']
schoolrecord = nls97[schoolrecordlist]

# initialize a KNN imputation model and fill values
impKNN = KNNImputer(n_neighbors=5)
newvalues = impKNN.fit_transform(schoolrecord)
schoolrecordimp = pd.DataFrame(newvalues, columns=schoolrecordlist, index=schoolrecord.index)

# view imputed values
schoolrecord.head().T
schoolrecordimp.head().T
schoolrecord[['gpaoverall','highestgradecompleted']].agg(['mean','count'])
schoolrecordimp[['gpaoverall','highestgradecompleted']].agg(['mean','count'])
