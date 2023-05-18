import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


"""
封装一些公共的Api，像点击、提交、输入等
"""


class BasicApi(object):
    def __init__(self, browsers, out_time=5):
        self.browser = browsers
        self.out_time = out_time

    def custom_click(self, element, method=By.ID):
        WebDriverWait(self.browser, self.out_time).until(ec.presence_of_element_located((method,
                                                                                         element))).click()

    def custom_sendKey(self, element, key, method=By.ID):
        WebDriverWait(self.browser, self.out_time).until(ec.presence_of_element_located((method,
                                                                                         element))).send_keys(key)

    def custom_clear(self, element, method=By.ID):
        WebDriverWait(self.browser, self.out_time).until(ec.presence_of_element_located((method,
                                                                                         element))).clear()

    def custom_submit(self, element, method=By.ID):
        WebDriverWait(self.browser, self.out_time).until(ec.presence_of_element_located((method,
                                                                                         element))).submit()

    def custom_isDisplay(self, element, method=By.ID):
        WebDriverWait(self.browser, self.out_time).until(ec.presence_of_element_located((method,
                                                                                         element))).is_displayed()

    def custom_isSelect(self, element, method=By.ID):
        WebDriverWait(self.browser, self.out_time).until(ec.presence_of_element_located((method,
                                                                                         element))).is_selected()

    def custom_isEnable(self, element, method=By.ID):
        WebDriverWait(self.browser, self.out_time).until(ec.presence_of_element_located((method,
                                                                                         element))).is_enabled()

    def custom_save_screenshot(self, path):
        self.browser.save_screenshot(path + '.png')

    def custom_isText_exit(self, key, times=5):
        if key in self.browser.page_source:
            return True
        else:
            return False


if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("http://www.baidu.com")

    # browser.find_element(By.XPATH, '//*[@id="kw"]').send_keys("hello")
    WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.ID, "kw"))).send_keys("hello")
    time.sleep(5)
