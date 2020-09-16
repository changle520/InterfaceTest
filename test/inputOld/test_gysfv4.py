#__author__:ipharmacare
# 2020/9/9

import pytest
from config import service_code
from common.interface import update_cfgvalue
from config import cfg_id,cfg_key,cfg_value
from pylib.checkfile import check_file
from pylib.check_moreorders import moreorders,get_drugnames

@pytest.fixture()
def update_config():
    '''初始化：更改配置项'''
    update_cfgvalue(cfg_id[1], cfg_key[0], cfg_value[1])   #启用'是否打通审方'
    update_cfgvalue(cfg_id[2], cfg_key[3], cfg_value[2])   # 禁用'过滤有效数据'

@pytest.mark.usefixtures('update_config')
class Test_CheckFile():
    '''验证统一接口传给业务系统的入参'''

    testfile='../../data/统一接口自动化测试用例.xls'
    sheetname='4.0_old'
    type={'opt':'REAL_OPT','ipt':'REAL_IPT'}
    service_code=service_code[0]

    @pytest.mark.skip()
    def test_GYSFV4_OLD_001(self):
        self.test_rlt=check_file(self.testfile,self.sheetname,'GYSFV4_OLD_001',self.service_code,self.type['opt'],7)
        print(self.test_rlt)
        self.recipe_status = [v for k, v in self.test_rlt if k == 'recipe_status']
        self.drug_return_flag = [v for k, v in self.test_rlt if k == 'drug_return_flag']
        assert self.recipe_status==[0] and self.drug_return_flag==[0]

    @pytest.mark.skip()
    def test_GYSFV4_OLD_002(self):
        self.test_rlt=check_file(self.testfile,self.sheetname,'GYSFV4_OLD_002',self.service_code,self.type['opt'],7)
        print(self.test_rlt)
        self.recipe_status = [v for k, v in self.test_rlt if k == 'recipe_status']
        self.despensing_num = [v for k, v in self.test_rlt if k == 'despensing_num']
        assert self.recipe_status==[1] and self.despensing_num==[-2,-2]

    @pytest.mark.skip()
    def test_GYSFV4_OLD_003(self):
        self.test_rlt=check_file(self.testfile,self.sheetname,'GYSFV4_OLD_003',self.service_code,self.type['opt'],7)
        print(self.test_rlt)
        recipe_status=[v for k,v in self.test_rlt if k=='recipe_status']
        despensing_num=[v for k,v in self.test_rlt if k=='despensing_num']
        assert recipe_status==[0] and despensing_num==[-2,2]

    @pytest.mark.skip()
    def test_GYSFV4_OLD_004(self):
        self.test_rlt=check_file(self.testfile,self.sheetname,'GYSFV4_OLD_004',self.service_code,self.type['opt'],7)
        print(self.test_rlt)
        self.recipe_status = [v for k, v in self.test_rlt if k == 'recipe_status']
        self.despensing_num = [v for k, v in self.test_rlt if k == 'despensing_num']
        assert self.despensing_num==[-2,-2]

    @pytest.mark.skip()
    def test_GYSFV4_OLD_005(self):
        self.test_rlt=check_file(self.testfile,self.sheetname,'GYSFV4_OLD_005',self.service_code,self.type['ipt'],7)
        print(self.test_rlt)
        self.order_status = [v for k, v in self.test_rlt if k == 'order_status']
        assert self.order_status==[-1]

    @pytest.mark.skip()
    def test_GYSFV4_OLD_006(self):
        self.test_rlt=check_file(self.testfile,self.sheetname,'GYSFV4_OLD_006',self.service_code,self.type['ipt'],7)
        print(self.test_rlt)
        self.order_status = [v for k, v in self.test_rlt if k == 'order_status']
        assert self.order_status==[0]

class Test_check_threerequests():
    '''校验第3次请求返回的结果是否正确'''
    testfile = '../../data/统一接口自动化测试用例.xls'
    sheetname = '4.0_old'
    type = {'opt': 'REAL_OPT', 'ipt': 'REAL_IPT'}
    service_code = service_code[0]

    @pytest.fixture(autouse=True)   #测试用例级别的初始化方法，每个用例都会执行一次
    def update_config(self):
        '''初始化：更改配置项'''
        update_cfgvalue(cfg_id[3], cfg_key[2], cfg_value[2])  # 启用'门诊GY_SF_V4接口是否返回干预结果'

    def test_GYSFV4_OLD_008(self):
        self.response_xml = moreorders(self.testfile, self.sheetname, 'GYSFV4_OLD_008', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.drug_name = [v for k, v in self.test_rlt if k == 'drug_name']
        assert "头孢丙烯片" not in self.drug_name

class Test_MergeOders():
    """验证统一接口合并医嘱场景"""

    testfile = '../../data/统一接口自动化测试用例.xls'
    sheetname = '4.0_old'
    type = {'opt': 'REAL_OPT', 'ipt': 'REAL_IPT'}
    service_code = service_code[0]

    @pytest.mark.skip()
    def test_GYSFV4_OLD_009(self):
        '''不合并历史处方'''
        self.response_xml=moreorders(self.testfile,self.sheetname,'GYSFV4_OLD_009',self.service_code,7)
        self.test_rlt=get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.drug_name=[v for k, v in self.test_rlt if k == 'drug_name']
        assert "头孢丙烯分散片" not in self.drug_name

    @pytest.mark.skip()
    def test_GYSFV4_OLD_010(self):
        '''合并历史处方'''
        self.response_xml=moreorders(self.testfile,self.sheetname,'GYSFV4_OLD_009',self.service_code,7)
        self.test_rlt=get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.drug_name=[v for k, v in self.test_rlt if k == 'drug_name']
        assert "头孢丙烯分散片"  in self.drug_name

    def test_GYSFV4_OLD_011(self):
        '''合并历史处方'''
        self.response_xml=moreorders(self.testfile,self.sheetname,'GYSFV4_OLD_011',self.service_code,7)
        self.test_rlt=get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.drug_name=[v for k, v in self.test_rlt if k == 'drug_name']
        assert "头孢丙烯分散片"  not in self.drug_name

    def test_GYSFV4_OLD_012(self):
        '''合并历史处方'''
        self.response_xml=moreorders(self.testfile,self.sheetname,'GYSFV4_OLD_012',self.service_code,7)
        self.test_rlt=get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.drug_name=[v for k, v in self.test_rlt if k == 'drug_name']
        assert "头孢丙烯分散片" in self.drug_name

if __name__ == '__main__':
    pytest.main(["-s","test_gysfv4.py"])