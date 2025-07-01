import pytest
from main import digits

# Sloth Bytes Tests
def test_digits_sloth_bytes():
    assert digits(1) == 0
    assert digits(10) == 9
    assert digits(100) == 189
    assert digits(2020) == 6969

# Edge Cases Tests
def test_digits_zero():
    with pytest.raises(ValueError):
        digits(0)

def test_digits_negative():
    with pytest.raises(ValueError):
        digits(-10)

def test_digits_large():
    # Just check it runs and returns an int
    result = digits(1000000)
    assert isinstance(result, int)
    assert result > 0

def test_digits_one_less_than_power_of_ten():
    # Edge case: just before a new digit length
    assert digits(9) == 8
    assert digits(99) == 187
    assert digits(999) == 2886
