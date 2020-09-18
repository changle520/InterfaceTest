cd C:\Users\ipharmacare\interface\InterfaceTest\test
pytest -sq  ./inputNew --alluredir=../report/tmp
allure generate ../report/tmp -o ../report/report --clean
