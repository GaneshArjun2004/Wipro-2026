import pytest

@pytest.fixture(scope="function")
def sample_numbers():
    print("\n[Fixture] Providing sample numbers")
    return 10, 5

@pytest.fixture(scope="module")
def app_name():
    print("\n[Fixture] Setting up app name")
    return "Calculator App"