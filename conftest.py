import pytest
@pytest.fixture(scope='session')
def login():
    print('登录操作1')
    yield "good"
    print("登出操作")
