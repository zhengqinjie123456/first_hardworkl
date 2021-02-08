import pytest
import allure


class Test_level():
    def test_level1(self):
        print("好的")
        allure.attach.file(r"D:\python_test\project_1\test_allure\A_txt.txt",name="name是重命名用的",
                           attachment_type=allure.attachment_type.TEXT)
    def test_level2(self):
        print("好的")
        allure.attach.file(r"D:\python_test\project_1\test_allure\A_txt.txt",name="name是重命名用的",
                           attachment_type=allure.attachment_type.TEXT)
