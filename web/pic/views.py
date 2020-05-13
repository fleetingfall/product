from flask import Blueprint,render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Map, Funnel, WordCloud
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from web.pic.service import *
from web.common.utils import set_ch
import seaborn as sns



bp=Blueprint("bp_pic",__name__,url_prefix="/tea/pic",static_folder="static",template_folder="templates")

'''
第二套
'''
#商品价格频数情况分析，直方图
@bp.route("/price_frequency")
def price_count():
    price=query_price()
    n, bins, patches=plt.hist(x=price,bins=30,color="orange",normed=True)
    plt.xlabel("商品价格")
    plt.ylabel("商品数量频数")
    set_ch()
    plt.title(u'不同价格的商品频数分布')
    path = "web/pic/static/price_frequency.png"
    # plt.savefig(path)
    plt.close()
    filename = path.replace("web/pic/static/", "")
    print(filename)
    return render_template("pic_base.html", filename=filename)

#商品的销量频数情况分析，直方图
@bp.route("/sales_frequency")
def sales_count():
    sales=query_sales()
    n, bins, patches=plt.hist(x=sales,bins=100,color="purple",normed=True)
    plt.xlabel("商品销量")
    plt.ylabel("商品数量频数")
    set_ch()
    plt.title('不同销量的商品频数分布')
    path = "web/pic/static/sales_frequency.png"
    # plt.savefig(path)
    plt.close()
    filename = path.replace("web/pic/static/", "")
    print(filename)
    return render_template("pic_base.html", filename=filename)

@bp.route("/province_count")
def province_count():
    province,count=query_province_count()
    plt.bar(left=range(len(count)),height=count,color="DeepSkyBlue")
    plt.xticks(range(len(province)),province,size="small",rotation=60,fontsize=10)
    set_ch()
    plt.title('不同省份商品数量分布')
    plt.xlabel("商品省份")
    plt.ylabel("商品数量")
    path = "web/pic/static/province_count.png"
    plt.savefig(path)
    plt.close()
    filename = path.replace("web/pic/static/", "")
    print(filename)
    return render_template("pic_base.html", filename=filename)

'''
第一套
'''
#不同价格区间的商品销量分布，水平条形图
@bp.route("/priceRange_count")
def priceRange_count():
    price,sales=query_priceRange_count()
    n=len(price)
    plt.figure(figsize=(8,6))
    plt.barh(range(n),sales,0.8)
    plt.yticks(range(n),price)
    plt.xlabel("商品销量")
    plt.ylabel("商品价格区间")
    set_ch()
    plt.title('不同价格区间商品的销量')
    path = "web/pic/static/priceRange_count.png"
    # plt.savefig(path)
    plt.close()
    filename=path.replace("web/pic/static/","")
    return render_template("pic_base.html", filename=filename)

#商品价格对销量的影响分析，散点图
@bp.route("/price_count_influence")
def price_count_influence():
    price,sales=query_price_salse()
    plt.scatter(price,sales)
    plt.xlabel("商品销量")
    plt.ylabel("商品价格")
    set_ch()
    plt.title('商品价格对销量的影响分析')
    path = "web/pic/static/price_count_influence.png"
    # plt.savefig(path)
    plt.close()
    filename = path.replace("web/pic/static/", "")
    return render_template("pic_base.html",filename=filename)


#商品价格对销售额的影响分析，回归线性分析图
@bp.route("/price_money_influence")
def price_money_influence():
    price,sales=query_price_salse()
    np.set_printoptions(suppress=True)
    price=np.array(price)
    sales=np.array(sales)
    GMV=price*sales
    data=np.vstack((price,sales,GMV))
    data=data.T
    df=pd.DataFrame(data,columns=["price","sales","GMV"])
    sns.regplot(x="price",y="GMV",data=df)
    set_ch()
    plt.title('商品价格对销售额的影响分析')
    path = "web/pic/static/price_money_influence.png"
    # plt.savefig(path)
    plt.close()
    filename = path.replace("web/pic/static/", "")
    return render_template("pic_base.html", filename=filename)


'''
第三套
'''
# @bp.route("/province_sales")
# def province_sales():
#     province,sales=query_province_sales()
#     plt.bar(left=range(len(sales)),height=sales,color="DarkOrange")
#     plt.xticks(range(len(province)),province,size="small",rotation=60,fontsize=10)
#     set_ch()
#     plt.title('不同省份商品销量分布')
#     plt.xlabel("商品省份")
#     plt.ylabel("商品数量")
#     path = "web/pic/static/province_sales.png"
#     plt.savefig(path)
#     plt.close()
#     filename = path.replace("web/pic/static/", "")
#     render_template("pic_base.html", filename=filename)
#     return ""

@bp.route("/type_sales")
def funnel_type_sales():
    type,sales=query_types_sales()
    c = (
        Funnel()
            .add("商品", [list(z) for z in zip(type,sales)],gap=1)
            .set_global_opts(title_opts=opts.TitleOpts(title="茶叶类型销量前十",pos_bottom=True))
    )

    path="web/pic/static/type_sales.png"
    # make_snapshot(engine=snapshot,file_name=c.render(),output_name=path)
    filename = path.replace("web/pic/static/", "")
    return render_template("pic_base.html", filename=filename)


@bp.route("/map_province")
def map_province_sales():
    province,sales = query_province_sales()
    c = (
        Map()
            .add("商品销量", [list(z) for z in zip(province, sales)], "china", is_map_symbol_show=False)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="不同省份商品销量分布"),
            visualmap_opts=opts.VisualMapOpts(max_=2000000)
        )
    )
    # c.render("web/pic/templates/map_province_sales.html")
    path = "web/pic/static/map_province.png"
    # make_snapshot(engine=snapshot, file_name=c.render(), output_name=path)
    filename = path.replace("web/pic/static/", "")
    return render_template("pic_base.html", filename=filename)


@bp.route("/map_fuj")
def map_fuj_sales():
    city,sales = query_fuj_sales()
    for i in range(len(city)):
        city[i]=city[i]+"市"
    c = (
        Map()
            .add("商品销量", [list(z) for z in zip(city, sales)], "福建", is_map_symbol_show=False)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="福建省城市商品销量分布"),
            visualmap_opts=opts.VisualMapOpts(max_=1420000,min_=900)
        )
    )
    # c.render("web/pic/templates/map_fuj_sales.html")
    path = "web/pic/static/map_fuj.png"
    # make_snapshot(engine=snapshot, file_name=c.render(), output_name=path)
    filename = path.replace("web/pic/static/", "")
    return render_template("pic_base.html", filename=filename)

@bp.route("/map_zhej")
def map_zhej_sales():
    city,sales = query_zhej_sales()
    for i in range(len(city)):
        city[i]=city[i]+"市"
    c = (
        Map()
            .add("商品销量", [list(z) for z in zip(city, sales)], "浙江", is_map_symbol_show=False)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="浙江省城市商品销量分布"),
            visualmap_opts=opts.VisualMapOpts(max_=800000,min_=200)
        )
    )
    # c.render("web/pic/templates/map_zhej.html")
    path = "web/pic/static/map_zhej.png"
    # make_snapshot(engine=snapshot, file_name=c.render(), output_name=path)
    filename = path.replace("web/pic/static/", "")
    return render_template("pic_base.html", filename=filename)


@bp.route("/wordcloud")
def wordcloud_tea() -> WordCloud:
    words=query_types_count()
    c = (
        WordCloud()
        .add("", words, word_size_range=[20, 100])
        .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud"))
    )
    # c.render("web/pic/templates/wordcloud.html")
    path = "web/pic/static/wordcloud.png"
    # make_snapshot(engine=snapshot, file_name=c.render(), output_name=path)
    filename = path.replace("web/pic/static/", "")
    return render_template("pic_base.html", filename=filename)

