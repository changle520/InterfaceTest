#__author__:ipharmacare
# 2020/9/10

from datetime import date
from common.operationxml import get_elecontent
from config import interface_path
from common.operationxls import OperationdXls

def getfilename(xml_str,type):
    '''
    获取服务器上统一接口传给下游的入参文件存放目录
    :return:
    '''

    #例如：'/data/interface/interface_unified/in_out_bak/2020-09-10/H0003/REAL_OPT/test_opt_002/INNER_AUDIT_CENTER/753581389437341696/'

    #获取当天的日期
    today=date.today()
    #获取入参中的hospital_code
    hospital_code=get_elecontent(xml_str,'base','hospital_code')
    #获取入参中的patient_id
    patient_id=get_elecontent(xml_str,'base','patient_id')
    #拼接目录名
    inner_dir=f"/{interface_path}/{today}/{hospital_code}/{type}/{patient_id}/INNER_AUDIT_CENTER/"
    return inner_dir


if __name__ == '__main__':
    # rxls = OperationdXls(r"C:\Users\ipharmacare\interface\InterfaceTest\data\统一接口自动化测试用例.xls")
    # rxls.read_xls('4.0_old')
    # xml = rxls.get_cellvalue(2, 7)
    # print(getfilename(xml,'REAL_OPT'))
    pass