import os
import pytest


def login():
    pytest.main(['../testcase_1.py', '-sv', '--alluredir', '../outFiles/report_source'])
    os.system('allure generate ../outFiles/report_source -o ../outFiles/report --clean')


def logout():
    pytest.main(['../libs/test_logout.py', '-sv', '--alluredir', '../outFiles/report_source'])
    os.system('allure generate ../outFiles/report_source -o ../outFiles/report --clean')


if __name__ == '__main__':
    logout()
