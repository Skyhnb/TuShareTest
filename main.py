import tushare as ts
from sqlalchemy import create_engine
from database_structure import Base
import mysql_functions as mf


#
engine = create_engine('mysql+pymysql://root:wxt19981229@localhost:3306/tusharetest', echo=True)
# print(dir(engine))
# 创建表结构
Base.metadata.create_all(engine)

# 初始化token及接口
ts.set_token('595f0e6b1a18a83d84c7771bae22a0564e83c2ad4ac7382eee28b192')
tushare_api = ts.pro_api()

# 获取股票列表数据
# mf.update_stock_basic(engine, tushare_api)

# 获取当日新闻数据
mf.update_news_today(engine, tushare_api)
