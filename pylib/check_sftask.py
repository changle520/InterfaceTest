#__author__:ipharmacare
# 2020/9/18

from common.operationxls import OperationdXls
from common.interface import interfaceApi
from common.operationxml import stringtoXML,get_allEle_change,update_xmlcontent
import re,time

def check_sftask(xlspath,sheetname,testno,servicecode,col):
    """校验审方任务列表的数据是否生成"""

    # 获取xml字符串
    rxls = OperationdXls(xlspath, sheetname)
    xml_str = rxls.get_xml(testno, col)

    # 修改xml字符串中的节点内容
    xml_rlt = update_xmlcontent(xml_str)

    #使用正则替换patient_id的值
    id="id"+str(time.time())
    new_xml=re.sub("(<patient_id>).*(</patient_id>)",f"\\1{id}\\2",xml_rlt)
    print(new_xml)
    # 发送请求
    # interfaceApi(servicecode, xml_rlt)

if __name__ == '__main__':
    check_sftask('../data/统一接口自动化测试用例.xls', '4.0_old', 'GYSFV4_OLD_007', 'GY_SF_V4', 7)