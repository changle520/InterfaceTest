#__author__:ipharmacare
# 2020/9/18

import pytest
from config import service_code
from common.interface import update_cfgvalue
from config import cfg_id,cfg_key,cfg_value,testfile,sheetname
from pylib.checkfile import check_file
from pylib.check_moreorders import moreorders,moreorders_havedel,get_drugnames


@pytest.fixture(scope="function",autouse=False)
def update_config_one(request):
    '''初始化：更改配置项:用于更改一个配置项'''
    update_cfgvalue(request.param['id'], request.param['key'], request.param['value'])
    print(request.param)

class Test_CheckFile():
    '''验证统一接口传给业务系统的入参'''

    type={'opt':'REAL_OPT','ipt':'REAL_IPT'}
    service_code=service_code[0]

    def test_GYSFV4_NEW_001(self):
        self.test_rlt=check_file(testfile,sheetname[1],'GYSFV4_NEW_001',self.service_code,self.type['ipt'],7)
        print(self.test_rlt)
        self.order_status = [v for k, v in self.test_rlt if k == 'order_status']
        assert self.order_status==[-1]

    def test_GYSFV4_NEW_002(self):
        self.test_rlt=check_file(testfile,sheetname[1],'GYSFV4_NEW_002',self.service_code,self.type['ipt'],7)
        print(self.test_rlt)
        self.order_status = [v for k, v in self.test_rlt if k == 'order_status']
        assert self.order_status==[0]


class Test_MergeOders():
    """验证统一接口合并医嘱场景"""

    type = {'opt': 'REAL_OPT', 'ipt': 'REAL_IPT'}
    service_code = service_code[0]

    def test_GYSFV4_NEW_004(self):
        self.response_xml = moreorders_havedel(testfile, sheetname[1], 'GYSFV4_NEW_004', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = [v for k, v in self.test_rlt if k == 'error_info']
        assert "头孢丙烯分散片与头孢丙烯片的作用机制相同" not in self.error_info

    @pytest.mark.parametrize("update_config_one",[{'id':cfg_id[3],'key':cfg_key[4],'value':cfg_value[0]}],indirect=True)
    def test_GYSFV4_NEW_005(self,update_config_one):
        self.response_xml = moreorders(testfile, sheetname[1], 'GYSFV4_NEW_005', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = [v for k, v in self.test_rlt if k == 'error_info']
        assert "头孢丙烯片与头孢丙烯分散片的作用机制相同" not in self.error_info

    @pytest.mark.parametrize("update_config_one",[{'id':cfg_id[3],'key':cfg_key[4],'value':cfg_value[1]}],indirect=True)
    def test_GYSFV4_NEW_006(self,update_config_one):
        self.response_xml = moreorders(testfile, sheetname[1], 'GYSFV4_NEW_006', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = [v for k, v in self.test_rlt if k == 'error_info']
        assert "头孢丙烯片与头孢丙烯分散片的作用机制相同。"  in self.error_info

    @pytest.mark.parametrize("update_config_one",[{'id':cfg_id[3],'key':cfg_key[4],'value':cfg_value[0]}],indirect=True)
    def test_GYSFV4_NEW_007(self,update_config_one):
        self.response_xml = moreorders(testfile, sheetname[1], 'GYSFV4_NEW_007', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.drug_name = [v for k, v in self.test_rlt if k == 'drug_name']
        assert "头孢丙烯分散片" not in self.drug_name

    @pytest.mark.parametrize("update_config_one",[{'id':cfg_id[3],'key':cfg_key[4],'value':cfg_value[1]}],indirect=True)
    def test_GYSFV4_NEW_008(self,update_config_one):
        self.response_xml = moreorders(testfile, sheetname[1], 'GYSFV4_NEW_008', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.drug_name = [v for k, v in self.test_rlt if k == 'drug_name']
        assert "头孢丙烯分散片" in self.drug_name

    @pytest.mark.parametrize("update_config_one",[{'id':cfg_id[3],'key':cfg_key[4],'value':cfg_value[1]}],indirect=True)
    def test_GYSFV4_NEW_009(self,update_config_one):
        self.response_xml = moreorders(testfile, sheetname[1], 'GYSFV4_NEW_009', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = [v for k, v in self.test_rlt if k == 'error_info']
        assert "头孢丙烯片与头孢丙烯分散片的作用机制相同。"  in self.error_info

    @pytest.mark.parametrize("update_config_one",[{'id':cfg_id[5],'key':cfg_key[5],'value':420}],indirect=True)
    def test_GYSFV4_NEW_010(self,update_config_one):
        '''就这一个用例要获取当前时间，待后面再完善'''
        self.response_xml = moreorders(testfile, sheetname[1], 'GYSFV4_NEW_010', self.service_code, 7)
        self.test_rlt = get_drugnames(self.response_xml)
        print(self.test_rlt)
        self.error_info = [v for k, v in self.test_rlt if k == 'error_info']
        assert "头孢丙烯片与头孢丙烯分散片的作用机制相同。"  not in self.error_info

if __name__ == '__main__':
    pytest.main(["-s","test_gysfv4.py"])


