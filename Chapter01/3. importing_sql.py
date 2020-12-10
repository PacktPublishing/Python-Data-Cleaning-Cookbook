# import pandas, pymssql, and mysql
import pandas as pd
import numpy as np
import pymssql
import mysql.connector
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 5)
pd.options.display.float_format = '{:,.2f}'.format

# set sql select statement to pull the data
query = "SELECT studentid, school, sex, age, famsize,\
  medu AS mothereducation, fedu AS fathereducation,\
  traveltime, studytime, failures, famrel, freetime,\
  goout, g1 AS gradeperiod1, g2 AS gradeperiod2,\
  g3 AS gradeperiod3 From studentmath"

# use the pymssql api and read_sql to retrieve and load data from a SQL Server instance
server = "pdcc.c9sqqzd5fulv.us-west-2.rds.amazonaws.com"
user = "pdccuser"
password = "pdccpass"
database = "pdcctest"
conn = pymssql.connect(server=server,
  user=user, password=password, database=database)
studentmath = pd.read_sql(query,conn)
conn.close()

# use the mysql api and read_sql to retrieve and load data from mysql
# this will result in the same file as with the pymssql 
host = "pdccmysql.c9sqqzd5fulv.us-west-2.rds.amazonaws.com"
user = "pdccuser"
password = "pdccpass"
database = "pdccschema"
connmysql = mysql.connector.connect(host=host,
  database=database,user=user,password=password)
studentmath = pd.read_sql(sqlselect,connmysql)
connmysql.close()

studentmath.dtypes
studentmath.head()

# rearrange columns and set an index
newcolorder = ['studentid', 'gradeperiod1', 'gradeperiod2',
  'gradeperiod3', 'school', 'sex', 'age', 'famsize',
  'mothereducation', 'fathereducation', 'traveltime',
  'studytime', 'freetime', 'failures', 'famrel',
  'goout']
studentmath = studentmath[newcolorder]
studentmath.studentid.count()
studentmath.studentid.nunique()
studentmath.set_index('studentid', inplace=True)
studentmath.count()

# add codes to data values
setvalues={"famrel":{1:"1:very bad",2:"2:bad",3:"3:neutral",
    4:"4:good",5:"5:excellent"},
  "freetime":{1:"1:very low",2:"2:low",3:"3:neutral",
    4:"4:high",5:"5:very high"},
  "goout":{1:"1:very low",2:"2:low",3:"3:neutral",
    4:"4:high",5:"5:very high"},
  "mothereducation":{0:np.nan,1:"1:k-4",2:"2:5-9",
    3:"3:secondary ed",4:"4:higher ed"},
  "fathereducation":{0:np.nan,1:"1:k-4",2:"2:5-9",
    3:"3:secondary ed",4:"4:higher ed"}}

studentmath.replace(setvalues, inplace=True)
setvalueskeys = [k for k in setvalues]
studentmath[setvalueskeys].memory_usage(index=False)

for col in studentmath[setvalueskeys].columns:
    studentmath[col] = studentmath[col].astype('category')

studentmath[setvalueskeys].memory_usage(index=False)

# take a closer look at the new values
studentmath['famrel'].value_counts(sort=False, normalize=True)
studentmath[['freetime','goout']].\
  apply(pd.Series.value_counts, sort=False, normalize=True)
studentmath[['mothereducation','fathereducation']].\
  apply(pd.Series.value_counts, sort=False, normalize=True)