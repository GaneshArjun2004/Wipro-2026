import pytest
import json
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from utilities.driver_factory import get_driver

@pytest.fixture(scope="module")
def test_data():
    with open("data/test_data.json") as f:
        return json.load(f)

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_login_and_search(driver, test_data):
    driver.get("https://www.coach.com")
    
    # Login
    login_page = LoginPage(driver)
    login_page.login_user(test_data["username"], test_data["password"])
    
    # Search
    search_page = SearchPage(driver)
    search_page.search_product(test_data["search_product"])
    
    product_title = search_page.get_first_product_title()
    
    # Assertions
    assert test_data["search_product"].lower() in product_title.lower(), \
        f"Expected product '{test_data['search_product']}' in search results"
