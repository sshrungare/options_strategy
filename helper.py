import json
import pandas as pd

f = open('data.json')
data = json.load(f)

nifty = 34584.35 #get nifty

df = pd.DataFrame(data)

def fetch_oi(df,expiry_dt):
    ce_values = [data['CE'] for data in df['records']['data'] if "CE" in data and data['expiryDate'] == expiry_dt]
    pe_values = [data['PE'] for data in df['records']['data'] if "PE" in data and data['expiryDate'] == expiry_dt]

    ce_dt = pd.DataFrame(ce_values).sort_values(['strikePrice'])
    pe_dt = pd.DataFrame(pe_values).sort_values(['strikePrice'])
    
    return ce_dt,pe_dt 

exp_date = '05-Aug-2021'

ce_df , pe_df  = fetch_oi(df,exp_date)

#print (ce_df,pe_df)

def moneyness_ce(nifty,strike_price):
    if strike_price == int(round(nifty, -2)):
        return  'ATM'
    elif strike_price > nifty:
        return 'OTM'
    elif strike_price < nifty:
        return 'ITM' 
    else:
        return None
 
ce_df['moneyness'] = ce_df.apply(lambda x: moneyness_ce(nifty, x['strikePrice']), axis=1)

ce_df.to_csv('bank.csv')
dd = ce_df.loc[:,['strikePrice','moneyness']]
dd.to_csv('bank.csv')
print(ce_df.loc[:,['strikePrice','moneyness']])