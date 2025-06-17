from base import get_driver

driver = get_driver()
driver.get("http://16.171.54.54:3000/cart")
assert "cart" in driver.current_url.lower()
print("✅ Cart page accessed")
driver.quit()
