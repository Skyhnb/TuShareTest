import pandas as pd
import sqlalchemy

import tushare_data as td


def __truncate_update(engine, data, table_name):
    """删除表中数据，追加新数据"""
    conn = engine.connect()
    conn.execute('truncate ' + table_name)

    data.to_sql(table_name, engine, if_exists='append', index=False,
                dtype={
                    'ts_code': sqlalchemy.types.NVARCHAR(length=10),
                    'symbol': sqlalchemy.types.NVARCHAR(length=10),
                    'name': sqlalchemy.types.NVARCHAR(length=10),
                    'area': sqlalchemy.types.NVARCHAR(length=5),
                    'industry': sqlalchemy.types.NVARCHAR(length=10),
                    'fullname': sqlalchemy.types.NVARCHAR(length=30),
                    'market': sqlalchemy.types.NVARCHAR(length=3),
                    'exchange': sqlalchemy.types.NVARCHAR(length=4),
                    'list_date': sqlalchemy.types.NVARCHAR(length=10),
                    'is_hs': sqlalchemy.types.NVARCHAR(length=1)
                })


def update_stock_basic(engine, tushare_api):
    """更新 股票列表数据"""
    data = td.get_stock_basic(tushare_api)
#    print(data)
    __truncate_update(engine, data, 'stock_basic')


def update_news_today(engine, tushare_api):
    """更新 当日新闻数据"""
    data = td.get_news_today(tushare_api)
#    print(data)
    data.to_sql('news', engine, if_exists='append', index=False)

