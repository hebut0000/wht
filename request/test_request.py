
import pytest
import math
import allure

def fun(x):
    return x + 1


@pytest.mark.less
def test_answer():
    assert fun(3) == 4

@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.less
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.less
def test_square():
    num = 7
    assert 7*7 == 40

@allure.severity(allure.severity_level.MINOR)
@pytest.mark.others
def test_quality():
    assert 10 ==11