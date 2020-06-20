import yaml
import pytest
from cal import Calculator

@pytest.mark.usefixtures("cal_fixture")
class TestA:

    @pytest.mark.parametrize(["a", "b","c"],
                             yaml.safe_load(open("./data_cal_add.yml"))["add"]
                             )
    def test_add(self,a,b,c):
        cal=Calculator()
        assert c==cal.add(a,b)

    @pytest.mark.parametrize(["a", "b","c"],
                             yaml.safe_load(open("./data_cal_sub.yml"))["sub"]
                             )
    def test_sub(self,a,b,c):
        cal=Calculator()
        assert c==cal.sub(a,b)


    @pytest.mark.parametrize(["a", "b","c"],
                             yaml.safe_load(open("./data_cal_mul.yml"))["mul"]
                             )
    def test_mul(self,a,b,c):
        cal=Calculator()
        assert c==cal.mul(a,b)


    @pytest.mark.parametrize(["a", "b","c"],
                             yaml.safe_load(open("./data_cal_div.yml"))["div"]
                             )
    def test_div(self,a,b,c):
        cal=Calculator()
        assert c==cal.div(a,b)

