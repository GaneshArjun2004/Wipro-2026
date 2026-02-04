from selenium import webdriver
import time

def test_browser_navigation():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://example.com")
    time.sleep(2)
    print("Home Title:", driver.title)

    driver.get("https://example.com/")
    time.sleep(2)
    print("Second Title:", driver.title)

    driver.back()
    time.sleep(2)
    print("After Back:", driver.title)

    driver.forward()
    time.sleep(2)
    print("After Forward:", driver.title)

    driver.refresh()
    time.sleep(2)
    print("After Refresh:", driver.title)

    driver.quit()
