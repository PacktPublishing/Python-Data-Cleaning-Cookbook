# import pandas, json, pprint, and requests
import pandas as pd
import json
import os
import sys
import pprint
import requests
#import importlib
#importlib.reload(ci)

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 8)

# import the collection items module
sys.path.append(os.getcwd() + "/helperfunctions")
import collectionitem as ci

# load the art museum's json data
response = requests.get("https://openaccess-api.clevelandart.org/api/artworks/?african_american_artists")
camcollections = json.loads(response.text)
camcollections = camcollections['data']

# loop through the list creating a collection item instance each time
analysislist = []
for colldict in camcollections:
  coll = ci.Collectionitem(colldict)
  newdict = dict(id=colldict['id'],
    title=colldict['title'],
    type=colldict['type'],
    creationdate=colldict['creation_date'],
    ncreators=coll.ncreators(),
    ncitations=coll.ncitations(),
    birthyearsall=coll.birthyearsall(),
    birthyear=coll.birthyearcreator1())
  analysislist.append(newdict)

# create a pandas data frame
len(camcollections)
len(analysislist)
pprint.pprint(analysislist[0:1])
analysis = pd.DataFrame(analysislist)
analysis.birthyearsall.value_counts().head()
analysis.head(2)


