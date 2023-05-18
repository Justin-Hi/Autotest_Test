import time
from configs.config import config
import allure
import pytest

"""
登录接口，主要是测试测试用例的前置一些不重要的步骤
"""


@allure.feature('登录')
@allure.story('登录')
class Test_Login:
    @allure.step('输入用户名')
    def test_login1(self, basic_api):
        with allure.step('输入用户名'):
            basic_api.custom_sendKey(config.path_username, config.username, method='xpath')
        with allure.step('输入密码'):
            basic_api.custom_sendKey(config.path_password, config.password, method='xpath')
        with allure.step('点击登录按钮'):
            basic_api.custom_click(config.path_button, method='xpath')
        with allure.step('判断是否登录'):
            time.sleep(2)
            assert basic_api.custom_isText_exit(config.text_login) is True
        with allure.step('截图'):
            basic_api.custom_save_screenshot(config.path_screen)
            allure.attach.file(config.path_screen + '.png', attachment_type=allure.attachment_type.PNG)
