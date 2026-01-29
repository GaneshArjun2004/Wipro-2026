from test_Q1 import add

def test_app_name_fixture(app_name):
    assert app_name == "Calculator App"

def test_add_again(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 15