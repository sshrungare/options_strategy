
import requests
import json
import pandas as pd


new_url = 'https://www.nseindia.com/api/marketStatus'

headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(new_url,headers=headers)
dajs = json.loads(page.text)

f = open('data.json')
data = json.load(f)

nifty = 15778.45

print(type(data))

#def fetch_oi(expiry_dt):
#    ce_values = [data['CE'] for data in dajs['records']['data'] if "CE" in data and data['expiryDate'] == expiry_dt]
##    pe_values = [data['PE'] for data in dajs['records']['data'] if "PE" in data and data['expiryDate'] == expiry_dt]
##
##    ce_dt = pd.DataFrame(ce_values).sort_values(['strikePrice'])
##    pe_dt = pd.DataFrame(pe_values).sort_values(['strikePrice'])
##    
##    print(ce_dt[['strikePrice','lastPrice']])
##
##def main():
##    
##    expiry_dt = '27-Aug-2020'
##    fetch_oi(expiry_dt)#
#
#if __name__ == '__main__':
#    main()