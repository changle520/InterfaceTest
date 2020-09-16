#__author__:ipharmacare
# 2020/9/15

from common.operationxls import OperationdXls
from common.interface import interfaceApi
from common.operationxml import stringtoXML,get_allEle_change


def moreorders(xlspath,sheetname,testno,servicecode,col):
    '''连续发送请求'''

    #获取xml字符串
    rxls = OperationdXls(xlspath,sheetname)
    xml = rxls.get_xml(testno,col)
    xml_list=xml.split(",")   #将xml按逗号分隔

    #发送请求
    for xml in xml_list:
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print(xml)
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        response=interfaceApi(servicecode,xml)
    return response.text



def get_drugnames(response_xml):
    '''获取接口返回结果中的drug_name,用作断言'''
    xml_object=stringtoXML(response_xml)
    test_rlt = get_allEle_change(xml_object)
    return test_rlt

if __name__ == '__main__':
    xml=moreorders('../data/统一接口自动化测试用例.xls', '4.0_old', 'GYSFV4_OLD_012', 'GY_SF_V4', 7)
    print(xml)
    print(get_drugnames(xml))
    # print(moreorders('../data/统一接口自动化测试用例.xls', '4.0_old', 'GYSFV4_OLD_011','GY_SF_V4',7))