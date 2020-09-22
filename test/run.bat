cd C:\Users\ipharmacare\interface\InterfaceTest\test
pytest -sq inputOld/test_gysfv4.py::Test_CheckFile --alluredir=../report/tmp
allure generate ../report/tmp -o ../report/report --clean
