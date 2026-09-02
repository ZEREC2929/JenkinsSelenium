from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.google.com")
    driver.maximize_window()
    print("Website Title:", driver.title)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium WebDriver")
    search_box.submit()

    time.sleep(3)

    if "Selenium" in driver.title:
        print("TEST PASSED")
    else:
        print("TEST FAILED")

finally:
    driver.quit()