import requests
import json
import pandas as pd


new_url = 'https://www.nseindia.com/api/marketStatus'

headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(new_url,headers=headers)
dajs = json.loads(page.text)

with open('header.json', 'r') as outfile:
    print(outfile.readlines())

  