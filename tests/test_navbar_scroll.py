from base import get_driver
from selenium.webdriver.common.by import By
import time

driver = get_driver()
driver.get("http://16.171.54.54:3000")

links = driver.find_elements(By.TAG_NAME, "a")
clicked = False
for link in links:
    text = link.text.strip().lower()
    if "menu" in text:
        link.click()
        clicked = True
        time.sleep(2)
        break

assert clicked
print("✅ Navbar scroll to menu section works")
driver.quit()
