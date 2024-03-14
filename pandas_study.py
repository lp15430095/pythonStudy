import pandas as pd
import openpyxl
import xlrd
pd.set_option('display.unicode.east_asian_width',True)
pd.set_option('display.width',1000)
pd=pd.read_excel(r'C:\Users\Administrator'
                 r'\Desktop\鸿源'
                 r'.xlsx',sheet_name='Sheet1',header=1,index_col=None)
print(pd)
print('----------------------------------------------------')
# print(pd[['日期','货物名称']])
# print(pd.loc[[1,2],['数量/个','单价/元','总价/元']])
# print(pd.loc[(pd['数量/个']>=2.0) & (pd['总价/元']>=2000)])
pd['数据']=[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
list1=[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
pd.insert(loc=1,column='数据1',value=list1)
print(pd)