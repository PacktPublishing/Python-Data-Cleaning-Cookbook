# import the pandas, os, sys, and pprint libraries
import pandas as pd
import os
import sys
import pprint

# import the respondent class
sys.path.append(os.getcwd() + "/helperfunctions")
import respondent as rp
# import importlib
# importlib.reload(rp)
pd.set_option('display.width', 150)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)

# load the NLS data and then create a list of dictionaries
nls97 = pd.read_csv("data/nls97f.csv")
nls97list = nls97.to_dict('records')
nls97.shape
len(nls97list)
pprint.pprint(nls97list[0:1])

# loop through the list creating a respondent instance each time
analysislist = []
for respdict in nls97list:
  resp = rp.Respondent(respdict)
  newdict = dict(originalid=respdict['originalid'],
    childnum=resp.childnum(),
    avgweeksworked=resp.avgweeksworked(),
    age=resp.ageby('20201015'),
    baenrollment=resp.baenrollment())
  analysislist.append(newdict)

# create a pandas data frame
len(analysislist)
resp.respondentcnt
pprint.pprint(analysislist[0:2])
analysis = pd.DataFrame(analysislist)
analysis.head(2)
