from datetime import time
from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_class():
    @pytest.fixture()
    def fixture_test(self):
        self.driver=webdriver.Chrome()
        self.action=ActionChains(self.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        yield
        self.driver.quit()




    def test_move(self,fixture_test):
        self.driver.get("https://www.baidu.com")
        ele=self.driver.find_element_by_xpath('//div[@id="u1"]/span')
        self.action.move_to_element(ele)
        self.action.perform()
        sleep(3)




    def test_search(self,fixture_test):
        '''
        until放的是一个函数，注意函数不要用例括号，可以使用expected_conditions替代，需要导入包
        '''
        # def wait(x):
        #     return self.driver.find_element_by_id('kw')
        # WebDriverWait(self.driver,5).until(wait)
        
        # expected_conditions有各种方法，一般校验当前步骤的元素就可以了
        self.driver.get("https://www.baidu.com")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,'kw')))
        # self.driver.find_element_by_id('kw').send_keys('霍格沃兹测试学院')
        self.driver.find_element_by_xpath('//span//input[@id="kw"]').send_keys('霍格沃兹测试学院')
        self.driver.find_element_by_id('su').click()
        self.driver.find_element_by_link_text('霍格沃兹测试学院 - 主页').click()
        sleep(2)

    def test_actionchain(self,fixture_test):
        self.driver.get('http://sahitest.com/demo/clicks.htm')

        # 先定位要操作的元素，再使用ActionChains方法放入这些元素，最后调用perfrom()方法才会执行
        a=self.driver.find_element_by_xpath('//input[@value="click me"]')
        b=self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        c=self.driver.find_element_by_xpath('//input[@value="right click me"]')

        # 这一步非常重要
        action=ActionChains(self.driver)

        # 对应的方法分别是单击，双击，右键，然后分别传入要操作的元素
        action.click(a)
        action.double_click(b)
        action.context_click(c)
        action.perform()
        sleep(3)



