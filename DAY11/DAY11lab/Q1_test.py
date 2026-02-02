import pytest

@pytest.mark.parametrize("a,b,exp", [
    (1, 2, 3),
    (2, 3, 5),
    (5, 5, 10)
])
def test_add(a, b, exp):
    assert a + b == exp



def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="environment name"
    )


@pytest.fixture
def env(request):
    return  request.config.getoption("--env")



def test_env_option(env):
    assert env in ["dev", "qa", "prod"]


@pytest.mark.skip(reason="feature not implemented")
def test_skip_example():
    assert 1 == 1

@pytest.mark.xfail(reason="known bug")
def test_xfail_example():
    assert 1 == 0
