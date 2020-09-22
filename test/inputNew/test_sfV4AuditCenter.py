#__author__:ipharmacare
# 2020/9/18

import pytest
from pylib.checkfile import check_file
from config import service_code,testfile,sheetname
import allure

@allure.feature("校验给下游的入参")
@allure.story("新版本入参")
class Test_CheckFile():

    type = {'opt': 'REAL_OPT', 'ipt': 'REAL_IPT'}
    service_code=service_code[1]

    def test_SFV4AUDITCENTER_NEW_001(self):
        self.test_rlt = check_file(testfile,sheetname[1], 'SFV4AUDITCENTER_NEW_001',service_code,self.type['ipt'],7)
        print(self.test_rlt)
        self.order_status = [v for k, v in self.test_rlt if k == 'order_status']
        assert self.order_status == [-1]

    def test_SFV4AUDITCENTER_NEW_002(self):
        self.test_rlt = check_file(testfile,sheetname[1], 'SFV4AUDITCENTER_NEW_002',service_code,self.type['ipt'],7)
        print(self.test_rlt)
        self.order_status = [v for k, v in self.test_rlt if k == 'order_status']
        assert self.order_status == [0]




if __name__ == '__main__':
    pytest.main(["-s","test_sfV4AuditCenter.py::Test_CheckFile::test_SFV4AUDITCENTER_NEW_001"])