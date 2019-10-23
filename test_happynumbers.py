from happynumbers import get_happiness_state
from random import seed
from random import randint

def test_is_happy_one():
    assert True == get_happiness_state(1)

def test_is_happy_seven():
    assert True == get_happiness_state(7)

def test_is_happy_zero():
    assert False == get_happiness_state(0)

def test_is_happy_big_number():
    assert True == get_happiness_state(28907)