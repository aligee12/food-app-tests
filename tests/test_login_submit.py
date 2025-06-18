# from base import get_driver
# from selenium.webdriver.common.by import By
# import time

# driver = get_driver()
# driver.get("http://16.171.54.54:3000")
# driver.find_element(By.XPATH, "//button[contains(text(), 'sign in')]").click()
# time.sleep(1)

# driver.find_element(By.NAME, "email").send_keys("fake@example.com")
# driver.find_element(By.NAME, "password").send_keys("wrongpass")
# driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
# time.sleep(2)

# assert "login" in driver.page_source.lower() or "invalid" in driver.page_source.lower()
# print("✅ Login error handled properly")
# driver.quit()

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Use a relative import to get the driver from the 'base.py' file
from .base import get_driver

def test_login_failure_with_wrong_credentials():
    """
    Tests that submitting the login form with incorrect credentials shows an error.
    """
    base_url = os.getenv("TEST_URL", "http://localhost:3000")
    driver = get_driver()
    
    try:
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

        # Open the login modal
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'sign in')]"))).click()

        # Enter incorrect credentials
        wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("fake@example.com")
        driver.find_element(By.NAME, "password").send_keys("wrongpassword")
        
        # Click the final "Login" button inside the modal
        driver.find_element(By.XPATH, "//button[text()='Login']").click()

        # Assertion: Check for an error message. This assumes an error message element appears.
        # You may need to adjust the locator (e.g., By.CLASS_NAME, 'error-toast')
        error_message = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid') or contains(text(), 'incorrect')]"))
        )
        assert error_message.is_displayed()
        print("✅ ASSERTION PASSED: Login error message was displayed correctly.")

    finally:
        driver.quit()