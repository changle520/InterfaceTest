#__author__:ipharmacare
# 2020/9/9

import pytest
from config import service_code
from common.interface import update_cfgvalue
from common.connectmysql import config_data
from config import cfg_key,cfg_value,testfile,sheetname
from pylib.checkfile import check_file
from pylib.check_moreorders import moreorders,moreorders_havedel,moreorders_invaild,get_drugnames
import allure

@pytest.fixture(scope="class")
def update_config_more():
    '''初始化：更改配置项:用于更改多个配置项'''
    update_cfgvalue(config_data['sf_unicom_enable'], cfg_key[0], cfg_value[0])   #启用'是否打通审方'
    update_cfgvalue(config_data['filter_valid_data'], cfg_key[2], cfg_value[3])   # 禁用'过滤有效数据'

@pytest.fixture(scope="function",autouse=False)
def update_config_one(request):
    '''初始化：更改配置项:用于更改一个配置项'''
    update_cfgvalue(request.param['id'], request.param['key'], request.param['value'])
    print(request.param)


@allure.feature("验第3次请求返回的结果")
@allure.story("老版本入参")
class Test_check_threerequests():
    '''校验第3次请求返回的结果是否正确'''

    type = {'opt': 'REAL_OPT', 'ipt': 'REAL_IPT'}
    service_code = service_code[0]

    @pytest.mark.parametrize("update_config_one", [{'id':config_data['gy_result_by_prescription_enable'], 'key': cfg_key[3], 'value': cfg_value[2]}],
                             indirect=True)
    def test_GYSFV4_OLD_008(self,update_config_one):
        self.response_xml = moreorders(testfile, sheetname[0], 'GYSFV4_OLD_008', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = ",".join([v for k, v in self.test_rlt if k == 'error_info'])
        assert "头孢丙烯片" not in self.error_info

@allure.feature("校验多请求合并、不合并医嘱")
@allure.story("老版本入参")
class Test_MergeOders():
    """验证统一接口合并医嘱场景"""

    type = {'opt': 'REAL_OPT', 'ipt': 'REAL_IPT'}
    service_code = service_code[0]

    def test_GYSFV4_OLD_009(self):
        self.response_xml=moreorders(testfile,sheetname[0],'GYSFV4_OLD_009',self.service_code,7)
        self.test_rlt=get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = ",".join([v for k, v in self.test_rlt if k == 'error_info'])
        assert "头孢丙烯分散片" not in self.error_info

    def test_GYSFV4_OLD_010(self):
        self.response_xml=moreorders(testfile,sheetname[0],'GYSFV4_OLD_010',self.service_code,7)
        self.test_rlt=get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = ",".join([v for k, v in self.test_rlt if k == 'error_info'])
        assert "头孢丙烯分散片"  in self.error_info

    def test_GYSFV4_OLD_011(self):
        self.response_xml=moreorders(testfile,sheetname[0],'GYSFV4_OLD_011',self.service_code,7)
        self.test_rlt=get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = ",".join([v for k, v in self.test_rlt if k == 'error_info'])
        assert "头孢丙烯分散片"  not in self.error_info

    def test_GYSFV4_OLD_012(self):
        self.response_xml=moreorders(testfile,sheetname[0],'GYSFV4_OLD_012',self.service_code,7)
        self.test_rlt=get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = ",".join([v for k, v in self.test_rlt if k == 'error_info'])
        assert "头孢丙烯分散片" in self.error_info

    def test_GYSFV4_OLD_013(self):
        self.response_xml = moreorders_havedel(testfile, sheetname[0], 'GYSFV4_OLD_013', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = ",".join([v for k, v in self.test_rlt if k == 'error_info'])
        assert "头孢丙烯分散片" not in self.error_info

    @pytest.mark.parametrize("update_config_one",[{'id':config_data['gy_temporary_orders_effective_once_enable'],'key':cfg_key[4],'value':cfg_value[0]}],indirect=True)
    def test_GYSFV4_OLD_014(self,update_config_one):
        self.response_xml = moreorders(testfile, sheetname[0], 'GYSFV4_OLD_014', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = ",".join([v for k, v in self.test_rlt if k == 'error_info'])
        assert "头孢丙烯分散片" not in self.error_info

    @pytest.mark.parametrize("update_config_one",[{'id':config_data['gy_temporary_orders_effective_once_enable'],'key':cfg_key[4],'value':cfg_value[1]}],indirect=True)
    def test_GYSFV4_OLD_015(self,update_config_one):
        self.response_xml = moreorders(testfile, sheetname[0], 'GYSFV4_OLD_015', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = ",".join([v for k, v in self.test_rlt if k == 'error_info'])
        assert "头孢丙烯分散片"  in self.error_info

    @pytest.mark.parametrize("update_config_one",[{'id':config_data['gy_temporary_orders_effective_once_enable'],'key':cfg_key[4],'value':cfg_value[0]}],indirect=True)
    def test_GYSFV4_OLD_016(self,update_config_one):
        self.response_xml = moreorders(testfile, sheetname[0], 'GYSFV4_OLD_016', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = ",".join([v for k, v in self.test_rlt if k == 'error_info'])
        assert "头孢丙烯分散片" not in self.error_info

    @pytest.mark.parametrize("update_config_one",[{'id':config_data['gy_temporary_orders_effective_once_enable'],'key':cfg_key[4],'value':cfg_value[1]}],indirect=True)
    def test_GYSFV4_OLD_017(self,update_config_one):
        self.response_xml = moreorders(testfile, sheetname[0], 'GYSFV4_OLD_017', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = ",".join([v for k, v in self.test_rlt if k == 'error_info'])
        assert "头孢丙烯分散片" not in self.error_info

    @pytest.mark.parametrize("update_config_one",[{'id':config_data['gy_temporary_orders_effective_once_enable'],'key':cfg_key[4],'value':cfg_value[1]}],indirect=True)
    def test_GYSFV4_OLD_018(self,update_config_one):
        self.response_xml = moreorders(testfile, sheetname[0], 'GYSFV4_OLD_018', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = ",".join([v for k, v in self.test_rlt if k == 'error_info'])
        assert "头孢丙烯分散片"  in self.error_info

    @pytest.mark.parametrize("update_config_one",[{'id':config_data['gy_long_orders_valid_time_scope'],'key':cfg_key[5],'value':420}],indirect=True)
    def test_GYSFV4_OLD_019(self,update_config_one):
        self.response_xml = moreorders_invaild(testfile, sheetname[0], 'GYSFV4_OLD_019', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = ",".join([v for k, v in self.test_rlt if k == 'error_info'])
        assert "头孢丙烯分散片"  not in self.error_info

@allure.feature("校验给下游的入参")
@allure.story("老版本入参")
@pytest.mark.usefixtures('update_config_more')
# @pytest.mark.run(order=1)
class Test_CheckFile():
    '''验证统一接口传给业务系统的入参'''

    type={'opt':'REAL_OPT','ipt':'REAL_IPT'}
    service_code=service_code[0]


    def test_GYSFV4_OLD_001(self):
        self.test_rlt=check_file(testfile,sheetname[0],'GYSFV4_OLD_001',self.service_code,self.type['opt'],7)
        print(self.test_rlt)
        self.recipe_status = [v for k, v in self.test_rlt if k == 'recipe_status']
        # self.drug_return_flag = [v for k, v in self.test_rlt if k == 'drug_return_flag']
        assert self.recipe_status==[0]

    def test_GYSFV4_OLD_002(self):
        self.test_rlt=check_file(testfile,sheetname[0],'GYSFV4_OLD_002',self.service_code,self.type['opt'],7)
        print(self.test_rlt)
        self.recipe_status = [v for k, v in self.test_rlt if k == 'recipe_status']
        self.despensing_num = [v for k, v in self.test_rlt if k == 'despensing_num']
        assert self.recipe_status==[1] and self.despensing_num==[-2,-2]

    def test_GYSFV4_OLD_003(self):
        self.test_rlt=check_file(testfile,sheetname[0],'GYSFV4_OLD_003',self.service_code,self.type['opt'],7)
        print(self.test_rlt)
        recipe_status=[v for k,v in self.test_rlt if k=='recipe_status']
        despensing_num=[v for k,v in self.test_rlt if k=='despensing_num']
        assert recipe_status==[0] and despensing_num==[-2,2]

    def test_GYSFV4_OLD_004(self):
        self.test_rlt=check_file(testfile,sheetname[0],'GYSFV4_OLD_004',self.service_code,self.type['opt'],7)
        print(self.test_rlt)
        self.recipe_status = [v for k, v in self.test_rlt if k == 'recipe_status']
        self.despensing_num = [v for k, v in self.test_rlt if k == 'despensing_num']
        assert self.despensing_num==[-2,-2]

    def test_GYSFV4_OLD_005(self):
        self.test_rlt=check_file(testfile,sheetname[0],'GYSFV4_OLD_005',self.service_code,self.type['ipt'],7)
        print(self.test_rlt)
        self.order_status = [v for k, v in self.test_rlt if k == 'order_status']
        assert self.order_status==[-1]

    def test_GYSFV4_OLD_006(self):
        self.test_rlt=check_file(testfile,sheetname[0],'GYSFV4_OLD_006',self.service_code,self.type['ipt'],7)
        print(self.test_rlt)
        self.order_status = [v for k, v in self.test_rlt if k == 'order_status']
        assert self.order_status==[0]



if __name__ == '__main__':
    pytest.main(["-s","test_gysfv4.py::Test_MergeOders::test_GYSFV4_OLD_015"])