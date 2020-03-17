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

