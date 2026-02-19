import pytest
import os
import random
import string
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://automationexercise.com"
TIMEOUT = 30


def generate_email():
    return "user_" + ''.join(random.choices(string.ascii_lowercase, k=6)) + "@test.com"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get(BASE_URL)

    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs["driver"]
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        driver.save_screenshot(
            f"screenshots/{item.name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        )


def test_complete_ecommerce_flow(driver):

    wait = WebDriverWait(driver, TIMEOUT)

    # =============================
    # 1️⃣ REGISTRATION
    # =============================
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Signup / Login')]"))
    ).click()

    email = generate_email()

    driver.find_element(By.NAME, "name").send_keys("TestUser")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    wait.until(EC.element_to_be_clickable((By.ID, "id_gender1"))).click()

    driver.find_element(By.ID, "password").send_keys("Test@123")
    driver.find_element(By.ID, "first_name").send_keys("Test")
    driver.find_element(By.ID, "last_name").send_keys("User")
    driver.find_element(By.ID, "address1").send_keys("Street 1")
    driver.find_element(By.ID, "state").send_keys("State")
    driver.find_element(By.ID, "city").send_keys("City")
    driver.find_element(By.ID, "zipcode").send_keys("123456")
    driver.find_element(By.ID, "mobile_number").send_keys("9999999999")

    driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Created!']"))
    )

    driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]"))
    )

    assert "Logged in as" in driver.find_element(
        By.XPATH, "//a[contains(text(),'Logged in as')]"
    ).text

    # =============================
    # 2️⃣ SEARCH PRODUCT
    # =============================
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/products')]"))
    ).click()

    search_box = wait.until(
        EC.visibility_of_element_located((By.ID, "search_product"))
    )
    search_box.send_keys("Tshirt")
    driver.find_element(By.ID, "submit_search").click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='productinfo text-center']"))
    )

    # =============================
    # 3️⃣ VIEW PRODUCT (AD SAFE)
    # =============================
    view_product = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//a[text()='View Product'])[1]"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", view_product)
    driver.execute_script("arguments[0].click();", view_product)

    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product-information"))
    )

    assert driver.find_element(By.CLASS_NAME, "product-information").is_displayed()

    # =============================
    # 4️⃣ ADD TO CART
    # =============================
    add_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='button']"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
    driver.execute_script("arguments[0].click();", add_btn)

    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//u[text()='View Cart']"))
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.ID, "cart_info_table"))
    )

    cart_rows = driver.find_elements(By.XPATH, "//tr[contains(@id,'product-')]")
    assert len(cart_rows) > 0

    # =============================
    # 5️⃣ UPDATE QUANTITY
    # =============================
    qty = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_quantity_input"))
    )

    qty.clear()
    qty.send_keys("2")

    assert qty.get_attribute("value") == "2"

    # =============================
    # 6️⃣ REMOVE ITEM
    # =============================
    wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-times"))
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//b[text()='Cart is empty!']"))
    )

    assert driver.find_element(
        By.XPATH, "//b[text()='Cart is empty!']"
    ).is_displayed()

    # =============================
    # 7️⃣ LOGOUT
    # =============================
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Logout')]"))
    ).click()

    wait.until(EC.url_contains("login"))

    assert "login" in driver.current_url.lower()
import pytest
import os
import random
import string
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://automationexercise.com"
TIMEOUT = 30


def generate_email():
    return "user_" + ''.join(random.choices(string.ascii_lowercase, k=6)) + "@test.com"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get(BASE_URL)

    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs["driver"]
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        driver.save_screenshot(
            f"screenshots/{item.name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        )


def test_complete_ecommerce_flow(driver):

    wait = WebDriverWait(driver, TIMEOUT)

    # =============================
    # 1️⃣ REGISTRATION
    # =============================
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Signup / Login')]"))
    ).click()

    email = generate_email()

    driver.find_element(By.NAME, "name").send_keys("TestUser")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

    wait.until(EC.element_to_be_clickable((By.ID, "id_gender1"))).click()

    driver.find_element(By.ID, "password").send_keys("Test@123")
    driver.find_element(By.ID, "first_name").send_keys("Test")
    driver.find_element(By.ID, "last_name").send_keys("User")
    driver.find_element(By.ID, "address1").send_keys("Street 1")
    driver.find_element(By.ID, "state").send_keys("State")
    driver.find_element(By.ID, "city").send_keys("City")
    driver.find_element(By.ID, "zipcode").send_keys("123456")
    driver.find_element(By.ID, "mobile_number").send_keys("9999999999")

    driver.find_element(By.XPATH, "//button[@data-qa='create-account']").click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Created!']"))
    )

    driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]"))
    )

    assert "Logged in as" in driver.find_element(
        By.XPATH, "//a[contains(text(),'Logged in as')]"
    ).text

    # =============================
    # 2️⃣ SEARCH PRODUCT
    # =============================
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/products')]"))
    ).click()

    search_box = wait.until(
        EC.visibility_of_element_located((By.ID, "search_product"))
    )
    search_box.send_keys("Tshirt")
    driver.find_element(By.ID, "submit_search").click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='productinfo text-center']"))
    )

    # =============================
    # 3️⃣ VIEW PRODUCT (Ad Safe)
    # =============================
    view_product = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//a[text()='View Product'])[1]"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", view_product)
    driver.execute_script("arguments[0].click();", view_product)

    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product-information"))
    )

    assert driver.find_element(By.CLASS_NAME, "product-information").is_displayed()

    # =============================
    # 4️⃣ ADD TO CART
    # =============================
    add_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='button']"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
    driver.execute_script("arguments[0].click();", add_btn)

    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//u[text()='View Cart']"))
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.ID, "cart_info_table"))
    )

    # Verify product exists
    cart_rows = driver.find_elements(By.XPATH, "//tr[contains(@id,'product-')]")
    assert len(cart_rows) > 0

    # Verify quantity displayed
    quantity_text = driver.find_element(
        By.XPATH, "//td[@class='cart_quantity']"
    ).text

    assert quantity_text != ""

    # =============================
    # 5️⃣ REMOVE ITEM
    # =============================
    wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-times"))
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//b[text()='Cart is empty!']"))
    )

    assert driver.find_element(
        By.XPATH, "//b[text()='Cart is empty!']"
    ).is_displayed()

    # =============================
    # 6️⃣ LOGOUT
    # =============================
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Logout')]"))
    ).click()

    wait.until(EC.url_contains("login"))

    assert "login" in driver.current_url.lower()