import allure
import pytest

#@pytest.mark.xfail
@pytest.mark.great
@allure.severity(allure.severity_level.BLOCKER)
def test_greater():
    num = 100
    assert num > 100

#@pytest.mark.xfail
@pytest.mark.great
@allure.severity(allure.severity_level.NORMAL)
def test_greater_equal():
    num = 100
    assert num >= 100

#@pytest.mark.skip
@pytest.mark.others
@allure.severity(allure.severity_level.MINOR)
def test_less():
    num = 100
    assert num < 200
