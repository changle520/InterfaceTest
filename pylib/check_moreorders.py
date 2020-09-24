#__author__:ipharmacare
# 2020/9/15

from common.operationxls import OperationdXls
from common.interface import interfaceApi
from common.operationxml import stringtoXML,get_allEle_change,update_xmlcontent
from common.usebs4 import usebs4forxml
import time
from datetime import datetime,timedelta

def moreorders(xlspath,sheetname,testno,servicecode,col):
    '''连续发送请求,servicecode一样'''

    #获取xml字符串
    rxls = OperationdXls(xlspath,sheetname)
    xml = rxls.get_xml(testno,col)
    xml_list=xml.split(",")   #将xml按逗号分隔

    #发送请求
    for xml in xml_list:

        #更改xml中的节点内容
        xml_str=update_xmlcontent(xml)
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print(xml_str)
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        response=interfaceApi(servicecode,xml_str)
        time.sleep(1)

    return response.text

def moreorders_invaild(xlspath,sheetname,testno,servicecode,col):
    '''连续发送请求,失效时间配置项的测试'''

    #获取xml字符串
    rxls = OperationdXls(xlspath,sheetname)
    xml = rxls.get_xml(testno,col)
    xml_list=xml.split(",")   #将xml按逗号分隔

    tomtime = datetime.now()  # 获取当前时间

    #发送请求
    for i in range(len(xml_list)):

        #更改xml中的节点内容
        xml_str = update_xmlcontent(xml_list[i])
        if i==0:
            #修改失效时间小于当前时间5分钟以内
            invaild_time=tomtime-timedelta(minutes=4)
            invaild_time_str = invaild_time.strftime("%Y-%m-%d %H:%M:%S")
            xml_str=usebs4forxml(xml_str,'order_invalid_time',invaild_time_str)
        if i==2:
            #修改失效时间小于当前时间10分钟以上
            invaild_time = tomtime - timedelta(minutes=11)
            invaild_time_str = invaild_time.strftime("%Y-%m-%d %H:%M:%S")
            print(invaild_time_str)
            xml_str = usebs4forxml(xml_str, 'order_invalid_time', invaild_time_str)
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print(xml_str)
        response=interfaceApi(servicecode,xml_str)
        time.sleep(1)

    return response.text

def moreorders_havedel(xlspath,sheetname,testno,servicecode,col):
    '''连续发送请求,请求中有删除接口,此方法用于用例:GYSFV4_OLD_013'''

    #获取xml字符串
    rxls = OperationdXls(xlspath,sheetname)
    xml = rxls.get_xml(testno,col)
    xml_list=xml.split(",")   #将xml按逗号分隔

    #发送请求
    for i in range (len(xml_list)):

        # 更改xml中的节点内容
        xml_str = update_xmlcontent(xml_list[i])
        if i==1:
            response = interfaceApi('CANCEL_GROUP_DRUG_V4',xml_str)  #当循环第二次的时候将servicecode赋值：'CANCEL_GROUP_DRUG_V4'
        else:
            response=interfaceApi(servicecode,xml_str)

    return response.text


def get_drugnames(response_xml):
    '''获取接口返回结果中的drug_name,用作断言'''
    xml_object=stringtoXML(response_xml)
    test_rlt = get_allEle_change(xml_object)
    return test_rlt

if __name__ == '__main__':
    xml=moreorders('../data/统一接口自动化测试用例.xls', '4.0_old', 'GYSFV4_OLD_018', 'GY_SF_V4', 7)
    print(xml)
    print(get_drugnames(xml))
    # print(moreorders('../data/统一接口自动化测试用例.xls', '4.0_old', 'GYSFV4_OLD_011','GY_SF_V4',7))