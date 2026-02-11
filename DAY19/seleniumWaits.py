from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

# implicit wait
driver.implicitly_wait(10)
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium waits")

print("element located using implicit wait")

# explicit wait
wait = WebDriverWait(driver, 15)
search_button = wait.until(
    EC.element_to_be_clickable((By.NAME, "btnK"))
)

print("element clickable now")
search_button.click()

# fluent wait in python (using poll_frequency)
fluent_wait = WebDriverWait(
    driver,
    timeout=20,
    poll_frequency=2,
    ignored_exceptions=[NoSuchElementException]
)

result = fluent_wait.until(
    lambda d: d.find_element(By.ID, "search")
)

print("element available for interaction")

driver.quit()
