"""
写一些配置信息，如测试地址、端口、日志参数配置
"""
import time
import os
# from data.data_temp import list_data

now_time = time.time()


class config:
    url = r"https://xdi-beta.fts.aero:8443/?#/login"
    path_screen = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\outFiles\screenshot\\" + str(now_time)
    generate_path = r'D:\python_work\test\testCases\testcase_'
    tem_keyword = ['输入', '判断', '点击', '截图']
    dict_key = ['index_case', 'case_name', 'steps', 'methods', 'elements', 'params']
    data_path = r'D:\python_work\test\data\data.xls'
    username = 'chenyong'
    password = '123456'
    path_username = '/html/body/div/section/form/div[1]/div/div/input'
    path_password = '/html/body/div/section/form/div[2]/div/div/input'
    path_button = '/html/body/div/section/form/div[3]/div/button/span'
    text_login = '本月平均分'
    data_temp_path = r'D:\python_work\test\data\data_temp.py'


if __name__ == '__main__':
    # print(list_data[0]['steps'])
    # print(config.path_screen)
    pass
