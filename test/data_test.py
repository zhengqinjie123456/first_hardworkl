import pytest


@pytest.fixture(params=['a','b'])
def login():
    print('登录操作')

def test_1(login):
    print(f'用例1:{login}')
def test_2(login):
    print(f'用例2:{login}')

