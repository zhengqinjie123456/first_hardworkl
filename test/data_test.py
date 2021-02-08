import pytest
import time
def test_1():
    print('用例1')
def test_2(login):
    print(f'用例2:')
def test_a():
    assert True
def test_b():
    time.sleep(5)
    assert True
def test_c():
    assert 1==2
