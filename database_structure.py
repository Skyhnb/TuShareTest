from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

# 创建对象基类
Base = declarative_base()

# 股票列表
"""
is_hs	    str	N	是否沪深港通标的，N否 H沪股通 S深股通
list_status	str	N	上市状态： L上市 D退市 P暂停上市
exchange	str	N	交易所 SSE上交所 SZSE深交所 HKEX港交所(未上线)
"""
class StockBasic(Base):
    __tablename__ = 'stock_basic'

    ts_code = Column(String(10), primary_key=True)  # TS代码
    symbol = Column(String(10))                     # 股票代码
    name = Column(String(10))                       # 股票名称
    area = Column(String(5))                        # 所在地域
    industry = Column(String(10))                   # 所属行业
    fullname = Column(String(30))                   # 股票全称
    market = Column(String(3))                      # 市场类型（主板/中小板/创业板/科创板）
    exchange = Column(String(4))                    # 交易所代码
    list_date = Column(String(10))                  # 上市日期
    is_hs = Column(String(1))                       # 是否沪深港通标的，N否 H沪股通 S深股通


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, autoincrement=True)   # 序号计数作为自增主键
    datetime = Column(String(20))                                # 新闻时间
    content = Column(String(2000))                               # 内容
    title = Column(String(150))                                  # 标题
    channel = Column(String(20))                                 # 分类
    source = Column(String(5))                                   # 来源
