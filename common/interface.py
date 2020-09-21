#__author__:ipharmacare
# 2020/9/8

import requests,json
import hashlib
from config import *

def login():
    '''
    登录接口
    :param username:用户名
    :param passwd: 密码
    :return:
    '''
    url=f"http://{ip}:{system_port}/{login_api}"  #拼接url
    headers={ 'Content-Type':"application/json"} #定义header

    #对密码进行加密
    md5_obj=hashlib.md5()
    md5_obj.update(password.encode(encoding='utf-8'))
    md5_passwd=md5_obj.hexdigest()

    #定义接口的传参
    data={"name":username,"password":md5_passwd}

    response=requests.post(url,data=json.dumps(data),headers=headers)
    return response.cookies

def update_cfgvalue(id,key,value):
    '''
    修改配置文件
    :param id: 配置项的id
    :param key: 配置项的名字
    :param value: 配置项的值
    :return:
    '''
    url=f"http://{ip}:{interface_port}/{cfg_api}"  #拼接url
    headers={
                'Content-Type': "multipart/form-data"
            }
    data={
        "sysConfigList[0].configKey":key,
          "sysConfigList[0].configValue":value,
          "sysConfigList[0].id":id
            }
    response=requests.post(url,data,cookies=login())
    print('配置项修改成功')
    # print(response.json())


def interfaceApi(serviceCode,xml,post_type=1):
    '''
    对外统一接口api
    :param serviceCode:服务编码
    :param post_type:
    :return:
    '''
    url=f"http://{ip}:{interface_port}/{interface_api}"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    params={"charset":'UTF-8',"serviceCode":serviceCode,"post_type":post_type}
    data={"xml":xml}

    response=requests.post(url,params=params,data=data,headers=headers,cookies=login())
    return response

def startAuditWork():
    '''开始审方,可以接受审方任务'''
    url = f"http://{ip}:{system_port}/{startAudit_api}"
    response=requests.get(url,cookies=login())
    return response.json()

def getAuditIptList(patientid=""):
    '''
    获取审方任务列表
    :param patientid:
    :return:
    '''
    try:
        url=f'http://{ip}:{system_port}/{sfAuditList_api}'
        data={'patientId':patientid}
        response=requests.post(url,json=data,cookies=login())
        return response.json()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # login()
    # update_cfgvalue(27,"commons_old_version_interface_enable",'false')
    # rxls = OperationdXls(r"C:\Users\ipharmacare\interface\InterfaceTest\data\统一接口自动化测试用例.xls")
    # rxls.read_xls('4.0_old')
    # xml = rxls.get_cellvalue(2, 7)
    # xml_split = xml.split(',')
    # interfaceApi(service_code[0],xml_split[0])
    print(startAuditWork())
    print(getAuditIptList())

