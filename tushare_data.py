import time
import pandas as pd
import datetime


def get_stock_basic(tushare_api, retry_count=3, pause=2):
    """股票列表数据"""
    frame = pd.DataFrame()
    for i in range(retry_count):
        try:
            data = tushare_api.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,'
                                                                                'fullname,market,exchange,list_date,is_hs')
        except:
            time.sleep(pause)
        else:
            frame = frame.append(data)
            break

    return frame


def get_news_today(tushare_api, retry_count=3, pause=2):
    today = datetime.datetime.now()
    yesterday = (today - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    today = today.strftime('%Y-%m-%d')
    sources = ['sina', 'yuncaijing', 'eastmoney']
    source_name = {'sina': '新浪财经',
                   'yuncaijing': '云财经',
                   'eastmoney': '东方财富'}
    frame = pd.DataFrame()

    for i in sources:
        for j in range(retry_count):
            try:
                data = tushare_api.news(src=i, start_date=yesterday, end_date=today, fields='datetime,content,title')
                data['source'] = source_name[i]
            except:
                time.sleep(pause)
            else:
                frame = frame.append(data)
                break

    return frame


def get_daily(tushare_api, retry_count=3,  pause=2):
    today = datetime.datetime.now().strftime('%Y%m%d')
    frame = pd.DataFrame()

    for count in range(retry_count):
        try:
            data = tushare_api.daily(trade_date=today)
        except:
            time.sleep(pause)
        else:
            trade_date = data['trade_date']
            data = data.drop('trade_date', axis=1)
            trade_date_to_date = []
            for i in trade_date:
                i = datetime.datetime.strptime(i, '%Y%m%d').date()
                trade_date_to_date.append(i)
            data['trade_date'] = trade_date_to_date
            frame = frame.append(data)
            break

    return frame
