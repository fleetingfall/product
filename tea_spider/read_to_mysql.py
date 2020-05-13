import xlrd
import pymysql
import datetime
import re


#获取当前月份
def get_month():
    now_month=datetime.datetime.now()
    return now_month.strftime("%Y-%m")


def data_to_mysql():
    wb= xlrd.open_workbook("get_data/tea搜索结果.xls")
    sheets=wb.sheets()#[<xlrd.sheet.Sheet object at 0x000001FCC106FAC8>...]
    print("连接数据库.....")
    #utf8, 而不是utf-8
    db=pymysql.connect(host="localhost",port=3306,user='root',password='123456',database='tea',use_unicode=True,charset="utf8")
    print("数据库连接成功")
    cursor = db.cursor()

    now_time=get_month()
    now_time="\""+now_time+"\""
    page=len(sheets)
    n=0
    for i in range(page):
        #获取表的行数
        nrow=sheets[i].nrows
        for j in range(1,nrow):
            row_values=sheets[i].row_values(j)
            #商品名称
            title=row_values[0].replace("<span class=H>","")
            title=title.replace("</span>","")
            title="\""+title.strip()+"\""

            #产品产地
            item_loc = row_values[3].split(" ")
            if len(item_loc)>1:
                province=item_loc[0]
                city = item_loc[1]
            else:
                province =city= item_loc[0]

            #row_values[1],row_values[2],"1",row_values[5],"U",row_values[7],'250',row_values[9],province,city,row_values[12],row_values[13],row_values[14],row_values[15],now_time
            #价格<float>
            view_price=float(row_values[1])

            view_fee="\""+row_values[2]+"\""
            #购买人数<int>
            people=row_values[4].replace("+","")
            people=people.replace("万","*10000")
            people=people.replace("人付款","")
            view_sales=eval(people)

            nick="\""+row_values[5]+"\""
            detail_url="\""+row_values[6]+"\""
            istmall="\""+row_values[7]+"\""
            warranty_period="\""+row_values[8]+"\""
            origin="\""+row_values[9]+"\""
            province="\""+province+"\""
            city="\""+city+"\""
            growth_season="\""+row_values[12]+"\""
            tea_type="\""+row_values[13]+"\""
            price_section="\""+row_values[14]+"\""
            # 净含量<int>
            net_content=row_values[15]
            if net_content!="":
                net_content = re.sub("\D", " ",row_values[15])
                net_content = net_content.strip()
                net_content = net_content.replace(" ", "*")
                net_content = re.sub(r'(\D)\1+',"*",net_content)
                net_content=eval(net_content)
            else:
                net_content=0
            sql="insert into tea_product(Title,View_Price,View_Fee,View_Sales,Nick,Detail_Url,isTmall,Warranty_Period,Origin,Province,City,Growth_Season, Tea_Type, Price_Section, Net_Content,Now_Time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"%(title,view_price,view_fee,view_sales,nick,detail_url,istmall,warranty_period,origin,province,city,growth_season, tea_type, price_section, net_content,now_time)
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
                n=n+1
                print("提交第%d条数据"%n)
            except Exception as e:
                print(e)
                # 发生错误时回滚
                db.rollback()
    # 关闭数据库连接
    db.close()

data_to_mysql()