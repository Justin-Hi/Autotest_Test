import xlrd
from configs.config import config
from template_test import template_auto
from data.data_temp import list_data

"""
此方法为处理excel表数据，即从excel表中将测试用例的编号、步骤、方法、元素、参数等读取到代码中；
并在data/ 目录下生成一个data_temp.py 文件用来临时存储测试用例和数据；以便后续自动生成测试脚本使用；
"""


class handle_xls:
    def __init__(self):
        self.data = xlrd.open_workbook(config.data_path)
        self.sheet1 = self.data.sheet_by_index(0)
        self.ncols = self.sheet1.ncols
        self.nrows = self.sheet1.nrows
        self.case_name = ''
        self.index_case = 0
        self.steps = []
        self.methods = []
        self.elements = []
        self.params = []
        self.data_temp = template_auto()
        self.data_temp.template_data_list1()

    def handle_xls(self):
        # list_datas = []
        with open(config.data_temp_path,  'w', encoding='utf-8') as w:
            for i in range(1, self.nrows):
                # list_data = []
                if self.sheet1.row_values(i)[1]:
                    # list_data.append('data_dict_' + str(i))
                    self.index_case = self.sheet1.row_values(i)[0]
                    self.case_name = self.sheet1.row_values(i)[2]
                    # list_data.append(self.case_name)
                    self.steps = self.string_to_list(self.sheet1.row_values(i)[3])
                    # list_data.append(self.steps)
                    self.methods = self.string_to_list(self.sheet1.row_values(i)[4])
                    # list_data.append(self.methods)
                    self.elements = self.string_to_list(self.sheet1.row_values(i)[5])
                    # list_data.append(self.elements)
                    self.params = self.string_to_list(self.sheet1.row_values(i)[6])
                    # list_data.append(self.params)
                    self.data_temp.template_data(index_case=int(self.index_case),
                                                 case_name=self.case_name,
                                                 steps=self.steps,
                                                 methods=self.methods,
                                                 elements=self.elements,
                                                 params=self.params)

                    # list_datas.append(list_data)
            # return list_datas
            w.write(self.data_temp.data_class_list1)
            w.flush()
            w.write('\n]\n')
        w.close()

    def string_to_list(self, string1):
        list1 = string1.split('\n')
        return list1


if __name__ == '__main__':
    handle_xls().handle_xls()