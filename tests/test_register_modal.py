from base import get_driver
from selenium.webdriver.common.by import By
import time

driver = get_driver()
driver.get("http://16.171.54.54:3000")
time.sleep(2)

try:
    # Step 1: Click the "sign in" button
    sign_in_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'sign in')]")
    sign_in_btn.click()
    print("✅ 'sign in' button clicked to open modal")
    time.sleep(1)

    # Step 2: Switch to Sign Up mode by clicking "Click here"
    switch_to_signup = driver.find_element(By.XPATH, "//p[contains(text(), 'Create a new account')]/span")
    switch_to_signup.click()
    print("✅ Switched to Sign Up mode")
    time.sleep(1)

    # Step 3: Check if name input field is now visible
    name_input = driver.find_element(By.NAME, "name")
    assert name_input
    print("✅ Register modal shows 'name' field")

except Exception as e:
    print("❌ Test failed:", str(e))

driver.quit()
