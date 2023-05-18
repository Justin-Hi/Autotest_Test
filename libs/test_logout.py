import time
from selenium import webdriver
from configs.config import config
from common.basicApi import BasicApi
import allure
import pytest

"""
登录接口，主要是测试测试用例的前置一些不重要的步骤
"""


@allure.feature('注销')
class Test_Logout:
    @allure.story('注销')
    def test_logout(self, basic_api):
        with allure.step('点击头像'):
            basic_api.custom_click(config.path_touxiang, 'xpath')
        with allure.step('点击注销按钮'):
            basic_api.custom_click(config.path_zhuxiao, 'class name')
        with allure.step('判断是否注销'):
            time.sleep(2)
            assert basic_api.custom_isText_exit(config.text_logout) is True
        with allure.step('截图'):
            basic_api.custom_save_screenshot(config.path_screen)
            allure.attach.file(config.path_screen + '.png', attachment_type=allure.attachment_type.PNG)
