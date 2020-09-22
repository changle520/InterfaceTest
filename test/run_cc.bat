cd C:\Users\ipharmacare\interface\InterfaceTest\test
pytest -sq  ./inputNew/test_sfV4ValidFlag.py::test_SFV4VALIDFLAG_NEW_001 --alluredir=../report/tmp
pytest -sq inputOld/test_gysfv4.py::Test_CheckFile --alluredir=../report/tmp
allure generate ../report/tmp -o ../report/report --clean
