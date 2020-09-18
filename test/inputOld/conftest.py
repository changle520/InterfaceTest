#__author__:ipharmacare
# 2020/9/9

import pytest
from common.interface import update_cfgvalue
from config import cfg_id,cfg_key,cfg_value

@pytest.fixture(scope='session',autouse=True)   #目录级别的初始化方法，该目录下只调用一次该方法
def openOldVersion():
    '''启用老版本接口'''
    update_cfgvalue(cfg_id[0],cfg_key[0],cfg_value[0])