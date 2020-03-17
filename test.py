import tushare as ts

ts.set_token('595f0e6b1a18a83d84c7771bae22a0564e83c2ad4ac7382eee28b192')
pro = ts.pro_api()
df = pro.news(src='yuncaijing', start_date='2020-03-09 00:00:00', end_date='2020-03-10 00:00:00',fields='datetime,content,title,'
                                                                                )
print(df)

