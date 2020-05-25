import tushare as ts
import datetime
import pandas as pd
import main

ts.set_token('595f0e6b1a18a83d84c7771bae22a0564e83c2ad4ac7382eee28b192')
pro = ts.pro_api()
df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20200315',
               fields='ts_code,trade_date,open,high,low,close,change,pct_chg')
trade_date = df['trade_date']

df = df.drop('trade_date', axis=1)


new_trade_date = []
for i in trade_date:
    i = datetime.datetime.strptime(i, '%Y%m%d').date()
    new_trade_date.append(i)



df['trade_date'] = new_trade_date

print(df)

df.to_sql('daily', main.engine, if_exists='append', index=False)