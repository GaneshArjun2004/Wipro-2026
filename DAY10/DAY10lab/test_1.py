import pytest
from test_Q1 import add, divide

# 🔧 xUnit style setup/teardown
def setup_module(module):
    print("\n[Setup Module] Starting calculator tests")

def teardown_module(module):
    print("\n[Teardown Module] Finished calculator tests")

def setup_function(function):
    print(f"\n[Setup Function] Running {function.__name__}")

def teardown_function(function):
    print(f"\n[Teardown Function] Finished {function.__name__}")


def test_add_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 15


def test_divide_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert divide(a, b) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)