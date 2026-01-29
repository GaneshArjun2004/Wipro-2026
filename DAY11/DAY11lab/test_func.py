import pytest

def login(user, pwd):
    if user == "admin" and pwd == "admin123":
        return "success"
    return "fail"


def test_login_success():
    result = login("admin", "admin123")
    assert result == "success"


def test_login_failure():
    result = login("user", "123")
    assert result == "fail"
