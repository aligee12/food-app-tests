from base import get_driver
from selenium.webdriver.common.by import By
import time

driver = get_driver()
driver.get("http://16.171.54.54:3000")
time.sleep(2)

food_items = driver.find_elements(By.CLASS_NAME, "food-item")
assert len(food_items) > 0
print(f"✅ {len(food_items)} food items rendered on menu")
driver.quit()
