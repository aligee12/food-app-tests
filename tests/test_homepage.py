from base import get_driver

driver = get_driver()
driver.get("http://16.171.54.54:3000")
assert "Small Bite" in driver.title  # Adjust this if needed
print("✅ Homepage loaded successfully")
driver.quit()
