import pandas as pd
import numpy as np
import os

# summarize panel data by group and time period
def adjmeans(df, byvar, var, period, changeexclude=None, excludetype=None):
  df = df.sort_values([byvar, period])
  df = df.dropna(subset=[var])

  # iterate using numpy arrays
  prevbyvar = 'ZZZ'
  prevvarvalue = 0
  rowlist = []
  varvalues = df[[byvar, var]].values

  # convert exclusion ratio to absolute number
  if (excludetype=="ratio" and changeexclude is not None):
    changeexclude = df[var].mean()*changeexclude

  # loop through variable values
  for j in range(len(varvalues)):
    byvar = varvalues[j][0]
    varvalue = varvalues[j][1]
    if (prevbyvar!=byvar):
      if (prevbyvar!='ZZZ'):
        rowlist.append({'byvar':prevbyvar, 'avgvar':varsum/byvarcnt,\
          'sumvar':varsum, 'byvarcnt':byvarcnt})
      varsum = 0
      byvarcnt = 0
      prevbyvar = byvar
  
    # exclude extreme changes in variable value
    if ((changeexclude is None) or (0 <= abs(varvalue-prevvarvalue) \
      <= changeexclude) or (byvarcnt==0)):
      varsum += varvalue
      byvarcnt += 1
  
    prevvarvalue = varvalue

  rowlist.append({'byvar':prevbyvar, 'avgvar':varsum/byvarcnt, \
    'sumvar':varsum, 'byvarcnt':byvarcnt})
  return pd.DataFrame(rowlist)

# check matches of merge-by values
def checkmerge(dfleft, dfright, mergebyleft, mergebyright):
  dfleft['inleft'] = "Y"
  dfright['inright'] = "Y"
  dfboth = pd.merge(dfleft[[mergebyleft,'inleft']],\
    dfright[[mergebyright,'inright']], left_on=[mergebyleft],\
    right_on=[mergebyright], how="outer")
  dfboth.fillna('N', inplace=True)
  print(pd.crosstab(dfboth.inleft, dfboth.inright))
  print(dfboth.loc[(dfboth.inleft=='N') | (dfboth.inright=='N')].head(20))

# concatenate all pickle files in a folder, assuming they have the same structure
def addfiles(directory):
  dfout = pd.DataFrame()
  columnsmatched = True

  # loop through the files
  for filename in os.listdir(directory):
    if filename.endswith(".csv"): 
      fileloc = os.path.join(directory, filename)

      # open the next file
      with open(fileloc) as f:
        dfnew = pd.read_csv(fileloc)
        print(filename + " has " + str(dfnew.shape[0]) + " rows.")
        dfout = pd.concat([dfout, dfnew])

        # check if current file has any different columns
        columndiff = dfout.columns.symmetric_difference(dfnew.columns)
        if (not columndiff.empty):
          print("", "Different column names for:", filename,\
            columndiff, "", sep="\n")
          columnsmatched = False
  print("Columns Matched:", columnsmatched)
  return dfout





