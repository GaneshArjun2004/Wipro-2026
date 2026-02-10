from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://letcode.in/alert")

time.sleep(2)

# 1. Trigger simple alert and accept
driver.find_element(By.ID, "accept").click()
alert = driver.switch_to.alert
print("Simple Alert Message:", alert.text)
alert.accept()

time.sleep(2)

# 2. Trigger confirmation alert and dismiss
driver.find_element(By.ID, "confirm").click()
alert = driver.switch_to.alert
print("Confirmation Alert Message:", alert.text)
alert.dismiss()

time.sleep(2)

# 3. Trigger prompt alert, enter text and accept
driver.find_element(By.ID, "prompt").click()
alert = driver.switch_to.alert
alert.send_keys("ganesh arjun")
print("Prompt Alert Message:", alert.text)
alert.accept()

time.sleep(2)

# 4. Verify result displayed on page
result = driver.find_element(By.ID, "myName").text
print("Result after prompt:", result)

driver.quit()
