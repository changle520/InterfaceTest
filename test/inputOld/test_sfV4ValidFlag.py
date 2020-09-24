#__author__:ipharmacare
# 2020/9/20

import pytest
from pylib.check_sftask import check_sftask
from config import cfg_key,cfg_value,testfile,sheetname
from common.interface import update_cfgvalue
from common.connectmysql import config_data
import allure

@pytest.fixture(scope="function",autouse=False)
def update_config_one(request):
    '''初始化：更改配置项:用于更改一个配置项'''
    update_cfgvalue(request.param['id'], request.param['key'], request.param['value'])
    print(request.param)
    yield
    update_cfgvalue(request.param['id'], request.param['key'], request.param['value_re'])  #清除

@allure.feature("校验审方列表生成任务")
@allure.story("老版本入参")
@pytest.mark.parametrize("update_config_one", [{'id': config_data['filter_valid_data'], 'key': cfg_key[2], 'value': cfg_value[2], 'value_re': cfg_value[3]}],
                             indirect=True)
def test_SFV4VALIDFLAG_OLD_001(update_config_one):
    test_rlt = check_sftask(testfile, sheetname[0], ['GYSFV4_OLD_007','SFV4VALIDFLAG_OLD_001'], ['GY_SF_V4','SF_V4_VALID_FLAG'], 7)
    print(test_rlt)
    assert test_rlt!=[] and test_rlt[0]==test_rlt[1]


if __name__ == '__main__':
    pytest.main(["-s","test_sfV4ValidFlag.py::test_SFV4VALIDFLAG_OLD_001"])