cd C:\Users\ipharmacare\interface\InterfaceTest\test
pytest -sq  ./inputNew/test_sfV4ValidFlag.py::test_SFV4VALIDFLAG_NEW_001 --alluredir=../report/tmp
allure generate ../report/tmp -o ../report/report --clean
