import  pytest

@pytest.fixture()
def a():
    print('3')
@pytest.fixture()
def test_b():

    print('--2')
    token = 12345
    yield token
    print('4')
def  test_c(test_b):
    token=test_b
    print(token)


