import pytest

@pytest.fixture(params=[[1,2],[3,4]],ids=['case1','case2'])
def login(request):

    return request.param
def test_1(login):

    print(f'用例1:{login}')
