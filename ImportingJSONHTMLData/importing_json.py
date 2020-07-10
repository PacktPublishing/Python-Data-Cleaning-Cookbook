# import pandas, numpy, json, pprint
import pandas as pd
import numpy as np
import json
import pprint
from collections import Counter
pd.set_option('display.width', 85)
pd.set_option('display.max_columns', 8)

# load tabular structure JSON data
with open('data/allcandidatenewssample.json') as f:
  candidatenews = json.load(f)

len(candidatenews)
pprint.pprint(candidatenews[0:2])
pprint.pprint(candidatenews[0]['source'])

Counter([len(item) for item in candidatenews])
pprint.pprint(next(item for item in candidatenews if len(item)<9))
pprint.pprint(next(item for item in candidatenews if len(item)>9))
pprint.pprint([item for item in candidatenews if len(item)==2][0:10])

candidatenews = [item for item in candidatenews if len(item)>2]
len(candidatenews)

# generate counts from JSON data
politico = [item for item in candidatenews if item["source"] == "Politico"]
len(politico)
pprint.pprint(politico[0:2])
sources = [item.get('source') for item in candidatenews]
type(sources)
len(sources)
sources[0:5]
pprint.pprint(Counter(sources).most_common(10))

# fix errors in values in dictionary
for newsdict in candidatenews:
    newsdict.update((k, "The Hill") for k, v in newsdict.items()
     if k == "source" and v == "TheHill")

sources = [item.get('source') for item in candidatenews]
pprint.pprint(Counter(sources).most_common(10))

# create a pandas data frame
candidatenewsdf = pd.DataFrame(candidatenews)
candidatenewsdf.dtypes
candidatenewsdf.rename(columns={'date':'storydate'}, inplace=True)
candidatenewsdf.storydate = candidatenewsdf.storydate.astype('datetime64[ns]')
candidatenewsdf.shape
candidatenewsdf.source.value_counts(sort=True).head(10)
