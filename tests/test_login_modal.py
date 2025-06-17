from base import get_driver
from selenium.webdriver.common.by import By
import time

driver = get_driver()
driver.get("http://16.171.54.54:3000")
login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'sign in')]")
login_button.click()
time.sleep(1)

email_field = driver.find_element(By.NAME, "email")
password_field = driver.find_element(By.NAME, "password")

assert email_field and password_field
print("✅ Login modal opened with fields")
driver.quit()
