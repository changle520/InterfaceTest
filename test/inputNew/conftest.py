#__author__:ipharmacare
# 2020/9/9

import pytest
from common.interface import update_cfgvalue
from common.connectmysql import config_data
from config import cfg_key,cfg_value

@pytest.fixture(scope='session',autouse=True)             #目录级别的初始化方法，该目录下只调用一次该方法
def closeOldVersion():
    '''禁用老版本接口'''
    update_cfgvalue(config_data['commons_old_version_interface_enable'],cfg_key[0],cfg_value[1])
    print('禁用老版本成功')
#     yield
#     openOldVersion()
#
# def openOldVersion():
#     '''开启老版本接口'''
#     update_cfgvalue(cfg_id[0], cfg_key[0], cfg_value[0])
#     print("清除操作完毕")