import pytest

def div(a, b):
    if b == 0:
        raise ValueError
    return a / b

def test_add():
    assert 2 + 3 == 5

def test_sub():
    assert 5 - 2 == 3

def test_mul():
    assert 3 * 4 == 12

def test_div():
    assert div(10, 2) == 5

def test_div_zero():
    with pytest.raises(ValueError):
        div(5, 0)
