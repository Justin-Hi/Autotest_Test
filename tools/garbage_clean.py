import os
import glob
import shutil


class total_path:
    basic_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_temp_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\data\\data_temp.py'
    log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\outFiles\\log\\'
    report_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\outFiles\\report'
    report_source_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\outFiles\\report_source'
    screenshot_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\outFiles\\screenshot\\'
    testCases_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\testCases\\'


class garbage_clean:
    def clean_data(self, data_temp_path):
        if os.path.exists(data_temp_path):
            os.remove(data_temp_path)

    def clean_log(self, log_path):
        clean_file = glob.glob(log_path + r'*.log')
        if clean_file:
            for i in clean_file:
                os.remove(i)

    def clean_report(self, report_path):
        if os.path.exists(report_path):
            shutil.rmtree(report_path)

    def clean_report_source(self, report_source_path):
        if os.path.exists(report_source_path):
            shutil.rmtree(report_source_path)

    def clean_screenshot(self, screenshot_path):
        clean_file = glob.glob(screenshot_path + r'*.png')
        if clean_file:
            for i in clean_file:
                os.remove(i)

    def clean_testcases(self, testCases_path):
        clean_file = glob.glob(testCases_path + r'testcase*.py')
        if clean_file:
            for i in clean_file:
                os.remove(i)

    def clean_running(self):
        self.clean_screenshot(total_path.screenshot_path)
        self.clean_report_source(total_path.report_source_path)
        self.clean_data(total_path.data_temp_path)
        # self.clean_log()
        # self.clean_testcases()
        # self.clean_report()


if __name__ == '__main__':
    # garbage_clean().clean_running()
    pass
