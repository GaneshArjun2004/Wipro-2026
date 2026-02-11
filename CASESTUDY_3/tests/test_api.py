import requests
import pytest

def test_get(base_url):
    r = requests.get(base_url)
    assert r.status_code == 200

@pytest.mark.parametrize("name,age", [
    ("A", 20),
    ("B", 30)
])
def test_post(base_url, name, age):
    r = requests.post(base_url, json={"name": name, "age": age})
    assert r.status_code == 201

@pytest.mark.skip
def test_skip():
    assert False

@pytest.mark.xfail
def test_fail():
    assert 1 == 2
