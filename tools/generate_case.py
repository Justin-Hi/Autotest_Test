from template_test import template_auto
from tools.handle_xls import handle_xls
from configs.config import config
from data.data_temp import list_data

"""
该方法用于生成测试脚本，自动读取/data/data_temp.py中的测试用例和数据，
自动完成测试脚本生成；
"""


class generate_cases:
    def __init__(self):
        self.temp = template_auto()

    def generate_class(self, title, class_name):
        self.temp.template_class(title=title, class_name=class_name)

    def generate_def(self, title, func_name):
        self.temp.template_def(story_title=title, function_name=func_name)

    def generate_click(self,title, index_case, index_step, method=''):
        self.temp.template_click(title=title,index_case=index_case,index_step=index_step,method=method)

    def generate_sendkey(self, title, index_case, index_step, method=''):
        self.temp.template_sendKey(title=title,index_case=index_case,index_step=index_step,method=method)

    def generate_panduan(self, title, index_case, index_step):
        self.temp.template_panduan(title=title,index_case=index_case,index_step=index_step)

    def generate_screen(self,title):
        self.temp.template_screen(title=title)

    def get_data(self, case_name, steps, methods, index_case, tem_keyword=config.tem_keyword):
        self.generate_class(title=case_name, class_name=case_name)
        self.generate_def(title=case_name, func_name=case_name)
        for i in range(len(steps)):
            # 输入
            if tem_keyword[0] in steps[i]:
                if methods[i] != 'null':
                    self.generate_sendkey(title=steps[i],
                                          index_case=index_case,
                                          index_step=i,
                                          method=methods[i])
                else:
                    self.generate_sendkey(title=steps[i],
                                          index_case=index_case,
                                          index_step=i)
            # 判断
            if tem_keyword[1] in steps[i]:
                self.generate_panduan(title=steps[i],
                                      index_case=index_case,
                                      index_step=i)
            #点击
            if tem_keyword[2] in steps[i]:
                if methods[i] != 'null':
                    self.generate_click(title=steps[i],
                                        index_case=index_case,
                                        index_step=i,
                                        method=methods[i])
                else:
                    self.generate_click(title=steps[i],
                                        index_case=index_case,
                                        index_step=i)
            # 截图
            if tem_keyword[3] in steps[i]:
                self.generate_screen(title=steps[i])
        return self.temp.import_code + self.temp.basic_code

    def generate_running(self):
        for i in range(len(list_data)):
            code = self.get_data(case_name=list_data[i][config.dict_key[1]],
                                 steps=list_data[i][config.dict_key[2]],
                                 methods=list_data[i][config.dict_key[3]],
                                 index_case=i)
            with open(config.generate_path + list_data[i][config.dict_key[0]] + '_' + list_data[i][config.dict_key[1]] + '.py', 'w', encoding='utf-8') as w:
                w.write(code)
            w.close()
            self.temp.template_basic_clear()


if __name__ == '__main__':
    handle_xls().handle_xls()
    generate_cases().generate_running()

