import pytest
def func(x):
    return x + 1

def test_1():
    assert func(3) == 5

def test2():
    assert func(4) == 5

def b():
    assert func(4) == 5

if __name__=="__main__":
    pytest.main(["test_a.py","-v"])