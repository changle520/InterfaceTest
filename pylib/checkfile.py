#__author__:ipharmacare
# 2020/9/10
from common.operationxls import OperationdXls
from common.interface import interfaceApi
from common.getfilename import getfilename
from common.sshlinux import get_file
from common.operationxml import get_xmlobject,get_allEle_change


def check_file(xlspath,sheetname,testno,servicecode,type,col):
    '''下载服务器上的落地文件到本地'''

    #获取xml字符串
    rxls = OperationdXls(xlspath,sheetname)
    xml_rlt = rxls.get_xml(testno,col)
    #发送请求
    interfaceApi(servicecode, xml_rlt)

    #拼接服务器上落地文件的路径
    scr_file=getfilename(xml_rlt,type)

    #连接服务器将落地文件找到并下载到本地
    target_file=get_file(scr_file)

    #解析xml,获取要校验的字段
    xml_obj=get_xmlobject(target_file)
    test_rlt= get_allEle_change(xml_obj)

    return test_rlt


if __name__ == '__main__':
    check_file('../data/统一接口自动化测试用例.xls', '4.0_old', 'GYSFV4_OLD_001','REAL_OPT',7)