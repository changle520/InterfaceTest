#__author__:ipharmacare
# 2020/9/20

import pytest
from pylib.check_sftask import check_sftask
from config import testfile,sheetname


def test_SFV4VALIDFLAG_NEW_001():
    test_rlt = check_sftask(testfile, sheetname[1], ['GYSFV4_NEW_003','SFV4VALIDFLAG_NEW_001'], ['GY_SF_V4','SF_V4_VALID_FLAG'], 7)
    print(test_rlt)
    assert test_rlt[0]==test_rlt[1]


if __name__ == '__main__':
    pytest.main(["-s","test_sfV4ValidFlag.py::test_SFV4VALIDFLAG_NEW_001"])