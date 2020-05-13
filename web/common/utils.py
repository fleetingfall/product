def results2dict(keys,values):
    if  not keys or not values:
        return {}
    return dict(zip(keys,values))

def results2list(keys,values):
    if keys is None or values  is None:
        return []
    return [results2dict(keys,value)for value in values]

#查询2列数据，分别存为列表
def values2list(values):
    if values is None:
        return []
    data1=[]
    data2=[]
    for data in values:
        data1.append(data[0])
        data2.append(data[1])
    return data1,data2

#查询1列数据，分别存为列表
def one_values2list(values):
    if values is None:
        return []
    data=[]
    for value in values:
        data.append(value[0])
    return data


class DBUtil:
    def __init__(self,orm):
        self.orm=orm

    def __enter__(self):
        self.session=self.orm.session
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            self.session.rollback()
        else:
            self.session.commit()



def set_ch():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体  
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
