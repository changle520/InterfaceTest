#__author__:ipharmacare
# 2020/9/18

from common.operationxls import OperationdXls
from common.interface import interfaceApi,startAuditWork,getAuditIptList
from common.operationxml import update_xmlcontent
from common.usebs4 import usebs4forxml
import time

def check_sftask(xlspath,sheetname,testno,servicecode,col):
    """校验审方任务列表的数据是否生成"""

    # 获取xml字符串
    rxls = OperationdXls(xlspath, sheetname)
    id = str(time.time())
    xml_list=[]
    patientid_value = id
    for i in range(len(testno)):
        xml_str = rxls.get_xml(testno[i],col)
        # 修改xml字符串中的节点内容
        xml_rlt = update_xmlcontent(xml_str)
        # 修改xml中的患者号
        xml_soup = usebs4forxml(xml_rlt, 'patient_id', patientid_value)
        xml_list.append(xml_soup.replace("\n",''))

    # 发送第一个请求-----GY_SF_V4
    # print(xml_list)
    interfaceApi(servicecode[0], xml_list[0])

    #开始审方
    startAuditWork()

    #获取审方列表的内容
    testone_rlt=getAuditIptList(patientid_value)
    print(testone_rlt)
    time.sleep(1)
    if testone_rlt['data']['engineInfos'] ==None: #如果审方列表没有生成对应的任务，继续发送第二个请求
        #发送第二个请求------SF_V4_VALID_FLAG
        interfaceApi(servicecode[1], xml_list[1])
        time.sleep(1)
        # 获取审方列表的内容
        testtwo_rlt = getAuditIptList(patientid_value)
        print(testtwo_rlt)
        rlt_patientid=testtwo_rlt['data']['engineInfos'][0]['patientId']
        return patientid_value,rlt_patientid
    else:
        return []





if __name__ == '__main__':
    print(check_sftask('../data/统一接口自动化测试用例.xls', '4.0_old', ['GYSFV4_OLD_007','SFV4VALIDFLAG_OLD_001'], ['GY_SF_V4','SF_V4_VALID_FLAG'], 7))