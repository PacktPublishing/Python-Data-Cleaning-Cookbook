# import pandas, numpy, and pyreadstat
import pandas as pd
import numpy as np
import pyreadstat
pd.set_option('display.max_columns', 5)
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.width', 75)

# retrieve spss data, along with the meta data
nls97spss, metaspss = pyreadstat.read_sav('data/nls97.sav')
nls97spss.dtypes
nls97spss.head()

nls97spss['R0536300'].value_counts(normalize=True)

# use column labels and value labels
metaspss.variable_value_labels['R0536300']
nls97spss['R0536300'].\
  map(metaspss.variable_value_labels['R0536300']).\
  value_counts(normalize=True)
nls97spss = pyreadstat.set_value_labels(nls97spss, metaspss, formats_as_category=True)
nls97spss.columns = metaspss.column_labels
nls97spss['KEY!SEX (SYMBOL) 1997'].value_counts(normalize=True)
nls97spss.dtypes
nls97spss.columns = nls97spss.columns.\
    str.lower().\
    str.replace(' ','_').\
    str.replace('[^a-z0-9_]', '')
nls97spss.set_index('pubid__yth_id_code_1997', inplace=True)

# apply the formats from the beginning
nls97spss, metaspss = pyreadstat.read_sav('data/nls97.sav', apply_value_formats=True, formats_as_category=True)
nls97spss.columns = metaspss.column_labels
nls97spss.columns = nls97spss.columns.\
  str.lower().\
  str.replace(' ','_').\
  str.replace('[^a-z0-9_]', '')
nls97spss.dtypes
nls97spss.head()
nls97spss.govt_responsibility__provide_jobs_2006.\
  value_counts(sort=False)
nls97spss.set_index('pubid__yth_id_code_1997', inplace=True)
 
# do the same for stata data
nls97stata, metastata = pyreadstat.read_dta('data/nls97.dta', apply_value_formats=True, formats_as_category=True)
nls97stata.columns = metastata.column_labels
nls97stata.columns = nls97stata.columns.\
    str.lower().\
    str.replace(' ','_').\
    str.replace('[^a-z0-9_]', '')
nls97stata.dtypes
nls97stata.head()
nls97stata.govt_responsibility__provide_jobs_2006.\
  value_counts(sort=False)
nls97stata.min()
nls97stata.replace(list(range(-9,0)), np.nan, inplace=True)
nls97stata.min()
nls97stata.set_index('pubid__yth_id_code_1997', inplace=True)

# pull sas data, using the sas catalog file for value labels
nls97sas, metasas = pyreadstat.read_sas7bdat('data/nls97.sas7bdat', catalog_file='data/nlsformats3.sas7bcat', formats_as_category=True)
nls97sas.columns = metasas.column_labels
nls97sas.columns = nls97sas.columns.\
    str.lower().\
    str.replace(' ','_').\
    str.replace('[^a-z0-9_]', '')
nls97sas.head()
nls97sas.keysex_symbol_1997.value_counts()
nls97sas.set_index('pubid__yth_id_code_1997', inplace=True)
