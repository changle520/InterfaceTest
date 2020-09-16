#__author__:ipharmacare
# 2020/9/10

import xml.etree.ElementTree as etree
from common.operationxls import OperationdXls
from config import check_tag

#定义一个全局变量，存放要获取的节点内容



def stringtoXML(text_str):
    '''将字符串转换为xml对象'''
    return etree.fromstring(text_str)

def get_xmlobject(path):
    '''
    将xml文件转换成树结构对象,并获取root节点
    :param path:xml类型的文件名
    :return: 返回xml的root节点
    '''
    dom=etree.parse(path)
    root=dom.getroot()
    return root

def get_elecontent(xml_str,p_tagname,c_tagname):
    '''
    获取xml中指定节点的文本内容
    :param xml_str: 字符串格式的xml
    :param p_tagname: 父节点
    :param c_tagname: 子节点
    :return:
    '''
    xml_object=stringtoXML(xml_str)
    for i in xml_object:
        if i.tag==p_tagname:
            return i.find(c_tagname).text


def get_allEle(rlt_list,fele):
    '''
    遍历xml中所有的节点,获取指定节点的内容
    :param fele:
    :return:
    '''

    for child in fele:

            if child.tag in check_tag:

                if child.text:
                    try:
                        value=int(eval(child.text))  #如果文本内容不为空,将xml中获取的数字转换为整型，便于后面测试用例中的断言:用于字符串类型的数值转换成数值型
                    except:
                        value=child.text             #不能满足上面的转换条件会抛异常,如:头孢丙烯片,所以捕获异常，直接赋值，不进行转换
                    rlt_list.append((child.tag,value))

                else:
                    value = child.text
                    rlt_list.append((child.tag, value))
            get_allEle(rlt_list,child)   #调用函数自己本身
    return rlt_list


#定义一个局部变量,调用获取节点的接口,获取所有的节点,保证每次读取的xml内容是独立的
def get_allEle_change(fele):
    rlt_list = []
    return get_allEle(rlt_list,fele)


if __name__=='__main__':
    # rxls = OperationdXls(r"C:\Users\ipharmacare\interface\InterfaceTest\data\统一接口自动化测试用例.xls")
    # rxls.read_xls('4.0_old')
    # xml = rxls.get_cellvalue(1, 7)
    # print(get_elecontent(xml,'base','hospital_code'))
    xml_obj=get_xmlobject("../data/innerIn/IN_test_opt_003_1599619328155_20200910161148386.txt")
    print(xml_obj)
    print(get_allEle_change(xml_obj))

