from cal import Calculator
import pytest
class TestCal:
    def test_add1(self):
        cal=Calculator()
        assert 3==cal.add(1,2)
    def test_add2(self):
        cal=Calculator()
        assert 300==cal.add(100,200)
    def test_div1(self):
        cal=Calculator()
        assert 3==cal.div(3,3)
    def test_div2(self):
        cal=Calculator()
        assert 0.5==cal.div(100,200)
    def test_sub1(self):
        cal=Calculator()
        assert 0==cal.sub(3,3)
    def test_sub2(self):
        cal=Calculator()
        assert -200==cal.sub(100,200)

if __name__=="__main__":
    pytest.main()