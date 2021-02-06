
# import yaml
#
# with open('./yamldata.yaml','r',encoding='utf-8') as r:
#     '''
#     windows环境下，读取yaml文件时不能出现中文，包括注释；
#     默认是使用gbk，所以这里需要定义一下utf-8
#     '''
#     a=yaml.safe_load(r)
# print(a)

'''
该装饰器传参的意思分别为:
第一个是对应函数的变量,顺序没要求
第二个是一个列表，列表里的值可以是列表或者元组，里面的列表或者元组都是一组数据，分别对应前面的变量
第三个ids是用例名称,也是个列表或者元组，数量要跟第二个参数一致
'''
import pytest
# @pytest.mark.parametrize("a,b",[(1,2),(2,3),[3,6]],ids=["1+2","2+3","3+6"])


@pytest.fixture()
def test_1(a,b):
    print(a+b)






