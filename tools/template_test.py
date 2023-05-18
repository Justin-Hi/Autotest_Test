from jinja2 import Template
from libs import test_login

template_import = """import time
from selenium import webdriver
from configs.config import config
from common.basicApi import BasicApi
from data.data_temp import list_data
from libs import test_login
from libs import test_logout
import allure
import pytest

# 生成的脚本为固定格式，如需更改，请生成后直接对脚本进行修改.
# 默认生成的测试用例为每个python文件只包含一条测试用例；

browser = webdriver.Chrome()
basic_api = BasicApi(browser)


"""

template_class = """
@allure.feature('{{feature_title}}')
class Test_{{class_name}}:
    def setup_class(self):
        # 该方法编写此类运行的前置条件，即不论此类下面有多少条测试用例，此方法都只运行一次；
        browser.get(config.url)
        {{function_body1}}
    def teardown_class(self):
        # 该方法编写此类运行的后置条件，即不论此类下面有多少条测试用例，此方法都只运行一次；
        browser.close()
        browser.quit()
        {{function_body2}}
    def setup(self):
        # 该方法编写每条测试用例运行的前置条件，开始测试每条测试用例前，该方法执行一次；如：
        print('此方法为测试用例前置条件')
        {{function_body3}}
        
    def teardown(self):
        # 该方法编写每条测试用例运行的后置条件，开始测试每条测试用例之后，该方法执行一次；如：
        print('此方法为测试用例后置条件')
        {{function_body4}}
        
"""
template_def = """
    @allure.story('{{story_title}}')
    def test_{{function_name}}(self):
"""

template_click = """
        with allure.step('{{step_title}}'):
            basic_api.custom_click(element=list_data[{{index_case}}][config.dict_key[4]][{{index_step}}],
                                   method='{{method}}')
            
"""

template_sendKeys = """
        with allure.step('{{step_title}}'):
            basic_api.custom_sendKey(element=list_data[{{index_case}}][config.dict_key[4]][{{index_step}}],
                                     key=list_data[{{index_case}}][config.dict_key[5]][{{index_step}}],
                                     method='{{method}}')
            
"""

template_isExit = """
        with allure.step('{{step_title}}'):
            time.sleep(2)
            assert basic_api.custom_isText_exit(key=list_data[{{index_case}}][config.dict_key[5]][{{index_step}}]) is True
            
"""

template_screenshot = """
        with allure.step('{{step_title}}'):
            basic_api.custom_save_screenshot(config.path_screen)
            allure.attach.file(config.path_screen + '.png', attachment_type=allure.attachment_type.PNG)
            
"""

template_data_list1 = """
list_data = [
"""

template_data = """
{   
    'index_case': '{{index_case}}',
    'case_name': '{{case_name}}',
    'steps': {{steps}},
    'methods': {{methods}},
    'elements': {{elements}},
    'params': {{params}}
    },
"""


class template_auto:
    def __init__(self):
        self.basic_code = ''
        self.import_code = Template(template_import).render()
        self.click_code = ''
        self.sendkey_code = ''
        self.panduan_code = ''
        self.screen_code = ''
        self.class_code = ''
        self.def_code = ''
        self.data_class_list1 = ''
        self.data_class_list2 = ''
        self.data_temp = ''

    def template_class(self, title, class_name, body1='', body2='', body3='pass', body4='pass'):
        self.class_code += Template(template_class).render(feature_title=title,
                                                           class_name=class_name,
                                                           function_body1=body1,
                                                           function_body2=body2,
                                                           function_body3=body3,
                                                           function_body4=body4)
        self.basic_code += self.class_code
        self.template_class_clear()

    def template_class_clear(self):
        self.class_code = ''

    def template_def(self,story_title, function_name):
        self.def_code += Template(template_def).render(story_title=story_title,
                                                       function_name=function_name)
        self.basic_code += self.def_code
        self.template_def_clear()

    def template_def_clear(self):
        self.def_code = ''

    def template_click(self, title,  index_case, index_step, method):
        self.click_code += Template(template_click).render(step_title=title,
                                                           index_case=index_case,
                                                           index_step=index_step,
                                                           method=method)
        self.basic_code += self.click_code
        self.template_click_clear()

    def template_click_clear(self):
        self.click_code = ''

    def template_sendKey(self, title, index_case, index_step, method):
        self.sendkey_code = Template(template_sendKeys).render(step_title=title,
                                                               index_case=index_case,
                                                               index_step=index_step,
                                                               method=method)
        self.basic_code += self.sendkey_code
        self.template_sendKey_clear()

    def template_sendKey_clear(self):
        self.sendkey_code = ''

    def template_panduan(self, title, index_case, index_step):
        self.panduan_code = Template(template_isExit).render(step_title=title,
                                                             index_case=index_case,
                                                             index_step=index_step)
        self.basic_code += self.panduan_code
        self.template_panduan_clear()

    def template_panduan_clear(self):
        self.panduan_code = ''

    def template_screen(self, title):
        self.screen_code = Template(template_screenshot).render(step_title=title)
        self.basic_code += self.screen_code
        self.template_screen_clear()

    def template_screen_clear(self):
        self.screen_code = ''

    def template_data_list1(self):
        self.data_class_list1 = Template(template_data_list1).render()

    def template_data(self, index_case, case_name, steps, methods, elements, params):
        self.data_temp = Template(template_data).render(index_case=index_case,
                                                        case_name=case_name,
                                                        steps=steps,
                                                        methods=methods,
                                                        elements=elements,
                                                        params=params)
        self.data_class_list1 += self.data_temp
        self.template_data_clear()

    def template_data_clear(self):
        self.class_code = ''

    def template_basic_clear(self):
        self.basic_code = ''
