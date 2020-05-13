import xlrd
import xlwt
import pandas as pd
from pandas import DataFrame


def merge_data():
    excel_path="get_data/tea搜索结果.xls"
    end_path="get_data/tea数据合并结果.xls"

    wb=xlrd.open_workbook(excel_path)
    sheets=wb.sheet_names()
    dataframe=DataFrame()

    for i in range(2):
        df=pd.read_excel(io=excel_path,sheet_name=sheets[i],header=0,index=False,encoding='utf8',)


        print(df)

merge_data()