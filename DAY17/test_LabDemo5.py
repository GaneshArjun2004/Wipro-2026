from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch in Edge
driver = webdriver.Edge()
driver.maximize_window()

# Part 1: Launch application
driver.get("https://demo.opencart.com/index.php?route=account/register")
time.sleep(3)

# Verify title
print("Title:", driver.title)

# Verify heading
heading = driver.find_element(By.TAG_NAME, "h1").text
print("Heading:", heading)

# Click Continue without data
driver.find_element(By.XPATH, "//button[text()='Continue']").click()
time.sleep(2)

# Verify warning message
warning = driver.find_element(By.CLASS_NAME, "alert-danger").text
print("Warning:", warning)

# Part 2: Personal details
driver.find_element(By.ID, "input-firstname").send_keys("Ganesh")
driver.find_element(By.ID, "input-lastname").send_keys("Arjun")
driver.find_element(By.ID, "input-email").send_keys("ganesh123@gmail.com")
driver.find_element(By.ID, "input-telephone").send_keys("9876543210")

# Part 3: Address
driver.find_element(By.ID, "input-address-1").send_keys("Hyderabad")
driver.find_element(By.ID, "input-city").send_keys("Hyderabad")
driver.find_element(By.ID, "input-postcode").send_keys("500001")

# Country dropdown
country = Select(driver.find_element(By.ID, "input-country"))
country.select_by_visible_text("India")
time.sleep(2)

# Region dropdown
region = Select(driver.find_element(By.ID, "input-zone"))
region.select_by_index(1)

# Part 4: Password
driver.find_element(By.ID, "input-password").send_keys("Test@123")
driver.find_element(By.ID, "input-confirm").send_keys("Test@123")

# Newsletter
driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()

# Privacy checkbox
driver.find_element(By.NAME, "agree").click()

time.sleep(2)

# Submit
driver.find_element(By.XPATH, "//button[text()='Continue']").click()
time.sleep(4)

# Verify success message
success = driver.find_element(By.TAG_NAME, "h1").text
print("Success:", success)

# Click Continue after success
driver.find_element(By.XPATH, "//a[text()='Continue']").click()

time.sleep(3)

# Open order history
driver.find_element(By.LINK_TEXT, "Order History").click()

time.sleep(3)

driver.quit()
