#__author__:ipharmacare
# 2020/9/9

import xlrd
from xlutils.copy import copy

class OperationdXls():
    '''读取excel文件内容'''
    def __init__(self,path,sheetname=None):
        '''
        根据文件路径打开excel
        :param path: 文件路径
        '''
        self.workbook=xlrd.open_workbook(path,formatting_info=True)

        if sheetname !=None:
            self.worksheet=self.workbook.sheet_by_name(sheetname)

    def read_xls(self,sheetname):
       '''
       读取指定表中的内容
       :param sheetname: 表名
       :return:
       '''
       self.worksheet= self.workbook.sheet_by_name(sheetname)
       return self.worksheet

    def get_rowvalue(self,row):
        '''获取某一行的值'''
        return self.worksheet.row_values(row)

    def get_cellvalue(self,row,col):
        '''
        获取某一个单元格的值
        :param row: 行
        :param col: 列
        :return: 单元格的值
        '''
        return self.worksheet.cell_value(row,col)

    def copy_xls(self):
        '''
        复制excel表格，用于保留原有测试用例的数据
        :return:
        '''
        copy_workbook=copy(self.workbook,)
        copy_workbook.save(r"C:\Users\ipharmacare\interface\InterfaceTest\data\统一接口自动化测试用例.xls")

    def get_xml(self,testno,col):
        '''
        根据用例名称编号，获取入参xml
        :param testno: 测试用例编号
        :param row: xml所在的列
        :return:
        '''
        self.rows=self.worksheet.nrows  #获得所有的行数
        #遍历行，拿到对应的xml
        for num in range(self.rows):
            self.row_content=self.get_rowvalue(num)
            if self.row_content[0]==testno:
                # print(self.row_content[col])
                return self.row_content[col]

if __name__ == '__main__':
    rxls=OperationdXls("../data/统一接口自动化测试用例.xls",'4.0_old')
    xml=rxls.get_xml('GYSFV4_OLD_001',7)
    print(xml)
    # rxls.copy_xls()
    # rxls.read_xls('4.0_old')
    # xml=rxls.get_cellvalue(5,7)
    # xml_split=xml.split(',')
    # for i in xml_split:
    #     print(i)
    #     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")