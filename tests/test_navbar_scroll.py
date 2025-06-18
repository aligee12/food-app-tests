# from base import get_driver
# from selenium.webdriver.common.by import By
# import time

# driver = get_driver()
# driver.get("http://16.171.54.54:3000")

# links = driver.find_elements(By.TAG_NAME, "a")
# clicked = False
# for link in links:
#     text = link.text.strip().lower()
#     if "menu" in text:
#         link.click()
#         clicked = True
#         time.sleep(2)
#         break

# assert clicked
# print("✅ Navbar scroll to menu section works")
# driver.quit()

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Use a relative import to get the driver from the 'base.py' file
from .base import get_driver

def test_navbar_scroll_to_menu():
    """
    Tests that clicking the 'Menu' link in the navigation bar scrolls to that section.
    """
    base_url = os.getenv("TEST_URL", "http://localhost:3000")
    driver = get_driver()

    try:
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

        # Find the 'Menu' link and click it. This is more direct than looping.
        menu_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(translate(., 'MENU', 'menu'), 'menu')]"))
        )
        menu_link.click()
        
        # To verify the scroll, we can check if the URL contains the anchor '#menu'
        # This assumes your link is an anchor link like <a href="#menu">
        wait.until(EC.url_contains("#menu"))

        # Assertion: Check the final URL
        assert "#menu" in driver.current_url
        print("✅ ASSERTION PASSED: Navbar scroll to menu section works.")

    finally:
        driver.quit()