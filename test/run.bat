cd C:\Users\ipharmacare\interface\InterfaceTest\test
pytest -sq  --alluredir=../report/tmp
allure generate ../report/tmp -o ../report/report --clean
