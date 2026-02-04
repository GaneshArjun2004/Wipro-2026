from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()   # make sure EdgeDriver is in PATH
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

# 1. Find elements using different locators and enter text

# By ID
driver.find_element(By.ID, "input-firstname").send_keys("Ganesh")

# By NAME
driver.find_element(By.NAME, "lastname").send_keys("Arjun")

# By CSS Selector
driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys("arjun789@gmail.com")

# By XPATH
driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("123456789")

# By CLASS NAME (used for confirm password just for demo)
driver.find_element(By.CLASS_NAME, "form-control").send_keys("Dummy")  
# (class is not unique, so better avoid in real tests)

# By XPATH (password)
driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("Test@123")

# By CSS
driver.find_element(By.CSS_SELECTOR, "#input-confirm").send_keys("Test@123")

# 2. Click checkbox and submit
driver.find_element(By.XPATH, "//input[@name='agree']").click()
driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()

time.sleep(3)

# 3. Validate message
msg = driver.find_element(By.CSS_SELECTOR, "#content h1").text

if msg == "Your Account Has Been Created!":
    print("Test Passed")
else:
    print("Test Failed")

driver.quit()