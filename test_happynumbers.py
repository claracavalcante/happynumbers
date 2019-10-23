from happynumbers import get_happiness_state
from random import seed
from random import randint

def test_is_happy_one():
    assert True == get_happiness_state(1)

def test_is_happy_seven():
    assert True == get_happiness_state(7)

def test_is_happy_big_number():
    seed(1)
    assert True == get_happiness_state(randint(0, 100))