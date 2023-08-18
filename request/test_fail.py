import pytest

import math
import allure

@allure.feature('test_success')
def test_sqrt_failure():
   num = 25
   assert math.sqrt(num) == 5

@allure.feature('test_success')
def test_square_failure():
   num = 7
   assert 7*7 == 49

@allure.feature('test_failure')
def test_equality_failure():
   assert 10 == 11


