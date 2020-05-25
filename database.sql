create table news
(
    id       int auto_increment
        primary key,
    datetime varchar(20)   null,
    content  varchar(2000) null,
    title    varchar(150)  null,
    source   varchar(5)    null
);

create table stock_basic
(
    ts_code   varchar(10) not null
        primary key,
    symbol    varchar(10) null,
    name      varchar(10) null,
    area      varchar(5)  null,
    industry  varchar(10) null,
    fullname  varchar(30) null,
    market    varchar(3)  null,
    exchange  varchar(4)  null,
    list_date varchar(10) null,
    is_hs     varchar(1)  null
);

create table daily
(
    ts_code    varchar(10) not null,
    trade_date datetime    not null,
    open       float       null,
    high       float       null,
    low        float       null,
    close      float       null,
    `change`   float       null,
    pct_chg    float       null,
    primary key (ts_code, trade_date)
)partition by range ( year(trade_date) )(
    partition p_2018 values less than (2019),
    partition p_2019 values less than (2020),
    partition p_2020 values less than (2021),
    partition p_future values less than (maxvalue)
    )


select
 partition_name part,
 partition_expression expr,
 partition_description descr,
table_rows
from information_schema.partitions  where
table_schema = schema()
and table_name='daily';


