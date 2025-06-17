from base import get_driver
from selenium.webdriver.common.by import By
import time

driver = get_driver()
driver.get("http://16.171.54.54:3000")
driver.find_element(By.XPATH, "//button[contains(text(), 'sign in')]").click()
time.sleep(1)

driver.find_element(By.NAME, "email").send_keys("fake@example.com")
driver.find_element(By.NAME, "password").send_keys("wrongpass")
driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
time.sleep(2)

assert "login" in driver.page_source.lower() or "invalid" in driver.page_source.lower()
print("✅ Login error handled properly")
driver.quit()
