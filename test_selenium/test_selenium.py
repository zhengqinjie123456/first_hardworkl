from datetime import time
from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_class():
    @pytest.fixture()
    def open_url(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(2)
        # self.driver.set_page_load_timeout(5)
        yield
        self.driver.quit()


    def test_search(self,open_url):
        '''
        until放的是一个函数，注意函数不要用例括号，可以使用expected_conditions替代，需要导入包
        '''
        # def wait(x):
        #     return self.driver.find_element_by_id('kw')
        # WebDriverWait(self.driver,5).until(wait)
        
        # expected_conditions有各种方法，一般校验当前步骤的元素就可以了
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,'kw')))
        self.driver.find_element_by_id('kw').send_keys('霍格沃兹测试学院')
        self.driver.find_element_by_id('su').click()
        self.driver.find_element_by_link_text('霍格沃兹测试学院 - 主页').click()
        sleep(2)


