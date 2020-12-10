# import pandas, numpy, json, pprint, and requests
import pandas as pd
import json
import pprint
import requests
import msgpack

pd.set_option('display.width', 85)
pd.set_option('display.max_columns', 8)

# load complicated JSON data from an API
response = requests.get("https://openaccess-api.clevelandart.org/api/artworks/?african_american_artists")
camcollections = json.loads(response.text)
len(camcollections['data'])
pprint.pprint(camcollections['data'][0])

# save to a json file
with open("data/camcollections.json","w") as f:
  json.dump(camcollections, f)

# read the json file
with open("data/camcollections.json","r") as f:
  camcollections = json.load(f)

pprint.pprint(camcollections['data'][0]['creators'])

# Write msgpack file
with open("data/camcollections.msgpack", "wb") as outfile:
    packed = msgpack.packb(camcollections)
    outfile.write(packed)

# Read msgpack file
with open("data/camcollections.msgpack", "rb") as data_file:
    msgbytes = data_file.read()

camcollections = msgpack.unpackb(msgbytes)

pprint.pprint(camcollections['data'][0]['creators'])

