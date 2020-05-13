from _ssl import SSLError

import xlwt
import requests
import re
import json
import time
from pyquery import PyQuery

#获取每页茶叶产品列表网页
def parser(url,page):
    head = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
            'cookie':"thw=cn; cna=i5nVEwafN2oCAWX02l4iXnqW; miid=473953852086556498; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=snow%5Cu7D2B%5Cu58A8; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; UM_distinctid=16705ef2238561-09ef1e58427d2b-2711d3e-144000-16705ef2239112e; enc=nZODvhUVtSsZTCL3rqmZcNYd1DVQywKd5BLf%2BS7FAJv9%2FLN2yykQQq6qujDkWDyiaA3Y7coUWpbyqjvxGzuaNA%3D%3D; t=ddaece9baceabdbfb51522e4b00974f7; cookie2=1c5da7e151214868b2f8a96804fa2c1a; _tb_token_=e53875e98835d; v=0; _m_h5_tk=b326ed45059bd624b60a9e261ee9c48b_1557133028485; _m_h5_tk_enc=f7f3826acbdc6761c14f7a49a088716f; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=113A5319129236F33995A74CAE189590; unb=2052636992; sg=%E5%A2%A829; _l_g_=Ug%3D%3D; skt=654167080462131c; cookie1=UIJ3kgKEUlEzwDsdLSdhwp2JihESd5%2BKsEWMg97U%2BPo%3D; csg=7b1100cb; uc3=vt3=F8dByEawPpThfrKZAaY%3D&id2=UUjUKIFHt3nKXQ%3D%3D&nk2=EFBp0iaVXjE%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; existShop=MTU1NzEyOTcwNw%3D%3D; lgc=snow%5Cu7D2B%5Cu58A8; _cc_=URm48syIZQ%3D%3D; dnk=snow%5Cu7D2B%5Cu58A8; _nk_=snow%5Cu7D2B%5Cu58A8; cookie17=UUjUKIFHt3nKXQ%3D%3D; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&pas=0&cookie14=UoTZ48QHY8ZPcw%3D%3D&tag=8&lng=zh_CN; mt=ci=88_1; isg=BGtrLkjCs30AL-igNoPm1MMn-o-VKH9lcRSv_N3o7qoBfIneY1APUgkK0rwS3Nf6; l=bBxuwyq7v3Iv_SBwBOfNZuI8a17tVIRbzsPzw4_G2ICP9LfM5u-AWZOn4u8HC3GVw6OHS387PXqQBeYBqxf.."
            }

    res=requests.get(url,headers=head,params={'s':page*44})
    html=res.text
    return html

#获取每个产品详情页
def details_parser(url):
    head = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        'cookie': "thw=cn; cna=i5nVEwafN2oCAWX02l4iXnqW; miid=473953852086556498; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=snow%5Cu7D2B%5Cu58A8; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; UM_distinctid=16705ef2238561-09ef1e58427d2b-2711d3e-144000-16705ef2239112e; enc=nZODvhUVtSsZTCL3rqmZcNYd1DVQywKd5BLf%2BS7FAJv9%2FLN2yykQQq6qujDkWDyiaA3Y7coUWpbyqjvxGzuaNA%3D%3D; t=ddaece9baceabdbfb51522e4b00974f7; cookie2=1c5da7e151214868b2f8a96804fa2c1a; _tb_token_=e53875e98835d; v=0; _m_h5_tk=b326ed45059bd624b60a9e261ee9c48b_1557133028485; _m_h5_tk_enc=f7f3826acbdc6761c14f7a49a088716f; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=113A5319129236F33995A74CAE189590; unb=2052636992; sg=%E5%A2%A829; _l_g_=Ug%3D%3D; skt=654167080462131c; cookie1=UIJ3kgKEUlEzwDsdLSdhwp2JihESd5%2BKsEWMg97U%2BPo%3D; csg=7b1100cb; uc3=vt3=F8dByEawPpThfrKZAaY%3D&id2=UUjUKIFHt3nKXQ%3D%3D&nk2=EFBp0iaVXjE%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; existShop=MTU1NzEyOTcwNw%3D%3D; lgc=snow%5Cu7D2B%5Cu58A8; _cc_=URm48syIZQ%3D%3D; dnk=snow%5Cu7D2B%5Cu58A8; _nk_=snow%5Cu7D2B%5Cu58A8; cookie17=UUjUKIFHt3nKXQ%3D%3D; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&pas=0&cookie14=UoTZ48QHY8ZPcw%3D%3D&tag=8&lng=zh_CN; mt=ci=88_1; isg=BGtrLkjCs30AL-igNoPm1MMn-o-VKH9lcRSv_N3o7qoBfIneY1APUgkK0rwS3Nf6; l=bBxuwyq7v3Iv_SBwBOfNZuI8a17tVIRbzsPzw4_G2ICP9LfM5u-AWZOn4u8HC3GVw6OHS387PXqQBeYBqxf.."
        }
    content = {}
    try:
        res = requests.get(url, headers=head,verify=False)
        html = res.text
        doc=PyQuery(html)
        li_doc=doc("#J_AttrUL").find('li')
        for doc in li_doc.items():
            data=doc.text().split("：")
            if len(data)<2:
                data=data[0].split(":")
            content[data[0]]=data[1].strip().replace("\xa0","")

    except SSLError as e:
        print("e")
    finally:
        return content

#分析每页产品列表网页的信息
def  analysis_html(html):
    # 使用正则表达式，找到g_page_config={}这行数据
    content = re.findall(r"g_page_config = .*g_srp_loadCss", html, re.S)[0]
    # 取出{}中的数据
    data = re.findall(r"{.*}", content)[0]
    # 将json数据转换成dic格式
    data = json.loads(data)
    return data

#分析每页产品列表网页的数据
def  analysis_data(data):
    tea_shop_list=data["mods"]["itemlist"]["data"]["auctions"]
    tea_data_list=[]
    for item in tea_shop_list:
        #https://detail.tmall.com/item.htm?id=2251723664&ali_refid=a3_430583_1006:1103300769:N:+VRb5MaRDCXAwqW+TgbBuQ==:7019f97e78799e2edaf3f7ab7a77ead9&ali_trackid=1_7019f97e78799e2edaf3f7ab7a77ead9
        if item['detail_url'][:6]!="https:":
            url="https:"+item['detail_url']
        else:
            url = item['detail_url']
        print(url)
        content = details_parser(url)
        temp={
            'title':item['title'],
            'view_price':item['view_price'],
            'view_fee':"是" if item['view_fee'] else "否",
            'item_loc':item['item_loc'],
            'view_sales':item['view_sales'],
            'nick':item['nick'],
            'detail_url': item['detail_url'],
            'isTmall':"是" if item['shopcard']['isTmall'] else "否",
            "保质期":content.get("保质期"),
            "产地": content.get("产地" ),
            "省份": content.get("省份" ),
            "城市": content.get("城市" ),
            "生长季节": content.get("生长季节" ),
            "茶种类": content.get("茶种类" ),
            "价格段": content.get("价格段" ),
            "净含量": content.get("净含量" ),

        }

        tea_data_list.append(temp)

    return tea_data_list


#将每页网页列表数据写入excle的sheet
def write_to_excle(f,data,page):
    tea_data_sheet=f.add_sheet('tea_data%d'%(page+1),cell_overwrite_ok=True)
    #写标题
    tea_data_sheet.write(0,0,"商品名称")
    tea_data_sheet.write(0,1,"商品价格")
    tea_data_sheet.write(0,2,"是否包邮")
    tea_data_sheet.write(0,3,"商品产地")
    tea_data_sheet.write(0,4,"购买人数")
    tea_data_sheet.write(0,5,"店铺名称")
    tea_data_sheet.write(0,6,"详情链接")
    tea_data_sheet.write(0,7,"是否天猫")
    tea_data_sheet.write(0, 8, "保质期")
    tea_data_sheet.write(0, 9, "产地")
    tea_data_sheet.write(0, 10, "省份")
    tea_data_sheet.write(0, 11, "城市")
    tea_data_sheet.write(0, 12, "生长季节")
    tea_data_sheet.write(0, 13, "茶种类")
    tea_data_sheet.write(0, 14, "价格段")
    tea_data_sheet.write(0, 15, "净含量")

    #内容
    for i in range(1,len(data)+1):
        j=i-1
        tea_data_sheet.write(i, 0, data[j]['title'])
        tea_data_sheet.write(i, 1, data[j]['view_price'])
        tea_data_sheet.write(i, 2, data[j]['view_fee'])
        tea_data_sheet.write(i, 3, data[j]['item_loc'])
        tea_data_sheet.write(i, 4, data[j]['view_sales'])
        tea_data_sheet.write(i, 5, data[j]['nick'])
        tea_data_sheet.write(i, 6, data[j]['detail_url'])
        tea_data_sheet.write(i, 7, data[j]['isTmall'])
        tea_data_sheet.write(i, 8, data[j]["保质期"])
        tea_data_sheet.write(i, 9, data[j]["产地"])
        tea_data_sheet.write(i, 10, data[j]["省份"])
        tea_data_sheet.write(i, 11, data[j]["城市"])
        tea_data_sheet.write(i, 12, data[j]["生长季节"])
        tea_data_sheet.write(i, 13, data[j]["茶种类"])
        tea_data_sheet.write(i, 14, data[j]["价格段"])
        tea_data_sheet.write(i, 15, data[j]["净含量"])

def main():
    url="https://s.taobao.com/search?q=%E8%8C%B6%E5%8F%B6"
    page=100
    f=xlwt.Workbook(encoding='utf-8')
    for i in range(page):
        html=parser(url,i)
        tea_data=analysis_html(html)
        tea_data_list=analysis_data(tea_data)
        write_to_excle(f,tea_data_list,i)
        time.sleep(1)

    f.save('get_data/tea搜索结果.xls')


main()
