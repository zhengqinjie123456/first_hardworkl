from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from test_selenium.base import BaseClass


class Test_class(BaseClass):


    def test_iframe(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # 如果frame没有id，定位可以使用相对定位找到这个标签
        a=self.driver.find_element_by_xpath('//*[@id="iframewrapper"]/iframe')
        self.driver.switch_to.frame(a)
        print(self.driver.find_element_by_id('draggable').text)

        # 回到上一级frame标签
        self.driver.switch_to.parent_frame()
        print(self.driver.find_element_by_id('submitBTN').text)


    def test_windowhandle(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_link_text('立即注册').click()

        # 查看当前窗口
        print(self.driver.current_window_handle)

        # 所有当前窗口
        a=self.driver.window_handles
        print(a)

        # 窗口信息是一个列表，切换到对应的列表即可
        self.driver.switch_to_window(a[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('abcd')
        sleep(3)

    def test_touchAction(self):
        self.driver.get('https://www.baidu.com/')
        a=self.driver.find_element_by_id('kw')
        a.send_keys('abcd')
        self.action.send_keys(Keys.ENTER).perform()
        self.touch_action.scroll_from_element(a,0,10000)
        self.touch_action.perform()

    def test_keyword(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        self.driver.find_element_by_xpath('//input[@type="textbox"]').click()
        self.action.send_keys("好样儿的")
        self.action.send_keys(Keys.SPACE).pause(1)
        self.action.send_keys('abc').pause(1)
        self.action.key_down(Keys.CONTROL).send_keys('a').pause(1)
        self.action.send_keys(Keys.BACKSPACE).pause(1)
        self.action.perform()
        sleep(3)


    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        darg_ele=self.driver.find_element_by_xpath('//*[@id="dragger"]')
        drop_ele=self.driver.find_element_by_xpath('//*[@class="item"][2]')
        #逻辑就是按住不放，移动到另一个元素，再松开鼠标
        # self.action.drag_and_drop(darg_ele,drop_ele).perform()
        # self.action.click_and_hold(darg_ele).release(drop_ele).perform()
        self.action.click_and_hold(darg_ele).move_to_element(drop_ele).release().perform()
        sleep(3)



    def test_move(self):
        self.driver.get("https://www.baidu.com")
        ele=self.driver.find_element_by_xpath('//div[@id="u1"]/span')
        self.action.move_to_element(ele)
        self.action.perform()
        sleep(3)




    def test_search(self):
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

    def test_actionchain(self):
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



