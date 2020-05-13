from flask import current_app

from web.common.utils import *

#第二套
def query_price():
    sql="SELECT View_Price FROM tea_product WHERE View_Price<4000;"
    with current_app.db as db:
        result_proxy=db.session.execute(sql)
        results=result_proxy.fetchall()
    return one_values2list(results)


def query_sales():
    sql="SELECT View_Sales FROM tea_product WHERE View_Sales<300000 AND View_Sales>0 ORDER BY View_Sales DESC;"
    with current_app.db as db:
        result_proxy=db.session.execute(sql)
        results=result_proxy.fetchall()
    return one_values2list(results)

def query_province_count():
    sql="SELECT Province,COUNT(Title) FROM tea_product GROUP BY Province;"
    with current_app.db as db:
        result_proxy=db.session.execute(sql)
        results=result_proxy.fetchall()
    return values2list(results)

#第一套
def query_price_salse():
    sql = "SELECT View_Price ,CAST(sum(View_Sales) AS SIGNED)  FROM tea_product  GROUP BY View_Price ORDER BY View_Price;"
    with current_app.db as db:
        result_proxy=db.session.execute(sql)
        #['View_Price', 'View_Sales']
        #[(108.0, 20000), (65.0, 6500), (15.0, 10000), (198.0, 3303),...]
        keys=result_proxy.keys()
        results=result_proxy.fetchall()
    return values2list(results)

def query_priceRange_count():
    sql="SELECT Price_Section,SUM(View_Sales) FROM tea_product WHERE Price_Section!='' GROUP BY Price_Section ORDER BY Price_Section;"
    with current_app.db as db:
        result_proxy=db.session.execute(sql)
        results=result_proxy.fetchall()
    return values2list(results)

#第三套
def query_types_sales():
    sql="SELECT Tea_Type,CAST(SUM(View_Sales) AS SIGNED) AS 'sales' FROM tea_product WHERE  Tea_Type!='' GROUP BY Tea_Type LIMIT 10;"
    with current_app.db as db:
        result_proxy=db.session.execute(sql)
        results=result_proxy.fetchall()
    return values2list(results)

def query_province_sales():
    sql="SELECT Province,CAST(SUM(View_Sales) AS SIGNED) AS 'sales' FROM tea_product GROUP BY Province ORDER BY sales DESC;"
    with current_app.db as db:
        result_proxy=db.session.execute(sql)
        results=result_proxy.fetchall()
    return values2list(results)

def query_fuj_sales():
    sql="SELECT City,CAST(SUM(View_Sales) AS SIGNED) AS 'sales' FROM tea_product WHERE Province='福建' GROUP BY City ORDER BY sales DESC;"
    with current_app.db as db:
        result_proxy=db.session.execute(sql)
        results=result_proxy.fetchall()
    return values2list(results)

def query_zhej_sales():
    sql="SELECT City,CAST(SUM(View_Sales) AS SIGNED) AS 'sales' FROM tea_product WHERE Province='浙江' GROUP BY City ORDER BY sales DESC;"
    with current_app.db as db:
        result_proxy=db.session.execute(sql)
        results=result_proxy.fetchall()
    return values2list(results)

#词云图
def query_types_count():
    sql="SELECT Tea_Type,CAST(COUNT(Title) AS SIGNED) AS 'count' FROM tea_product WHERE  Tea_Type!='' GROUP BY Tea_Type;"
    with current_app.db as db:
        result_proxy=db.session.execute(sql)
        results=result_proxy.fetchall()
    return results