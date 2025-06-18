# from base import get_driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = get_driver()
# driver.get("http://16.171.54.54:3000")

# try:
#     wait = WebDriverWait(driver, 30)  # Increased timeout

#     # Ensure food item image loads
#     wait.until(EC.presence_of_element_located((By.CLASS_NAME, "food-item-image")))
#     print("✅ Food items loaded")

#     # Check if item is already in cart
#     try:
#         green_icon = driver.find_element(By.CSS_SELECTOR, ".food-item-count .add-remove")
#         print("⚠️ Item already in cart, skipping add")
#         print(f"Green icon src: {green_icon.get_attribute('src')[:50]}...")  # Debug src
#     except:
#         # Click white 'add' icon
#         add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".food-item:first-child .add.add-remove")))
#         driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
#         driver.execute_script("arguments[0].click();", add_btn)
#         print("✅ Item added to cart")

#         # Confirm green icon (reliable locator)
#         green_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".food-item-count .add-remove")))
#         print("✅ Green '+' icon appeared")
#         print(f"Green icon src: {green_icon.get_attribute('src')[:50]}...")  # Debug src

#     # Navigate to cart page
#     driver.get("http://16.171.54.54:3000/cart")

#     # Confirm cart page loads
#     wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart")))
#     print("✅ Cart page loaded")

#     # Check cart items
#     cart_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart-items-title")))
#     assert len(cart_items) > 0, "❌ No items found in cart"
#     print(f"✅ Cart displays {len(cart_items)} item(s)")

# except Exception as e:
#     print("❌ Test failed")
#     print("Error:", str(e))
   

# finally:
#     driver.quit()

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Use a relative import to get the driver from the 'base.py' file in the same directory
from .base import get_driver

def test_cart_shows_added_item():
    """
    Adds an item to the cart from the homepage and verifies it appears on the cart page.
    """
    # Get the base URL from the environment variable
    base_url = os.getenv("TEST_URL", "http://localhost:3000")
    driver = get_driver()
    
    try:
        # Navigate to the homepage
        driver.get(base_url)
        wait = WebDriverWait(driver, 20) # Use a slightly shorter timeout

        # Ensure food items are loaded
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "food-item-image")))
        print("✅ Food items loaded on homepage")

        # Find the first food item on the page
        first_item = driver.find_element(By.CSS_SELECTOR, ".food-item")

        # Check if the item already has a counter (is already in the cart)
        try:
            first_item.find_element(By.CLASS_NAME, "food-item-count")
            print("⚠️ Item already in cart, proceeding to verification.")
        except:
            # If no counter, click the 'add' button to add it to the cart
            add_button = first_item.find_element(By.CSS_SELECTOR, ".add.add-remove")
            driver.execute_script("arguments[0].scrollIntoView(true);", add_button)
            driver.execute_script("arguments[0].click();", add_button)
            # Wait for the counter to appear as confirmation
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "food-item-count")))
            print("✅ Item added to cart.")
        
        # Navigate to the cart page
        cart_url = f"{base_url}/cart"
        driver.get(cart_url)

        # Wait for the main cart container to load
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart")))
        print("✅ Navigated to cart page.")

        # Assertion: Verify that there is at least one item listed in the cart
        cart_items = driver.find_elements(By.CLASS_NAME, "cart-item")
        assert len(cart_items) > 0, "Cart is empty, but it should contain at least one item."
        print(f"✅ ASSERTION PASSED: Cart displays {len(cart_items)} item(s).")

    finally:
        # Teardown: Always close the browser
        driver.quit()