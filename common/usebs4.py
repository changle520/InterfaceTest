#__author__:ipharmacare
# 2020/9/21
from bs4 import BeautifulSoup


def usebs4forxml(xml,ele,value):
    '''修改xml中节点的文本内容'''

    soup=BeautifulSoup(xml,'xml')
    content=soup.find(ele)
    content.string=value
    rlt=str(soup)
    return rlt
