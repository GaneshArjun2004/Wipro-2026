from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "search-input")
        self.search_button = (By.ID, "search-submit")
        self.product_title = (By.CSS_SELECTOR, ".product-name")

    def search_product(self, product_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_box)
        ).send_keys(product_name)
        self.driver.find_element(*self.search_button).click()

    def get_first_product_title(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.product_title)
        ).text
