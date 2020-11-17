# import pandas, numpy, json, pprint, and requests
import pandas as pd
import numpy as np
import json
import pprint
import requests

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 8)

# load more complicated data
response = requests.get("https://openaccess-api.clevelandart.org/api/artworks/?african_american_artists")
camcollections = json.loads(response.text)
print(len(camcollections['data']))
pprint.pprint(camcollections['data'][0])

# flatten the data
camcollectionsdf = pd.json_normalize(camcollections['data'], 'citations', ['accession_number','title','creation_date','collection','creators','type'])
print(camcollectionsdf.head(2).T)
creator = camcollectionsdf[0:1].creators[0]
print(type(creator[0]))
pprint.pprint(creator)
camcollectionsdf['birthyear'] = pd.to_numeric(camcollectionsdf.creators[0][0]['birth_year'])
print(camcollectionsdf.head(2).T)


