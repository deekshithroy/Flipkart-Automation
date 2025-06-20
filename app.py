# Flipkart Shopping Automation Script - Beginner Friendly
# This script automates login, search, add to cart, and checkout on Flipkart

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Global variable to store our browser
driver = None

def setup_browser():
    """Setup and open Chrome browser"""
    global driver
    print("Opening Chrome browser...")
    
    # Create Chrome browser instance
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("Browser opened successfully!")

def open_flipkart():
    """Open Flipkart website"""
    global driver
    print("Opening Flipkart website...")
    driver.get("https://www.flipkart.com")
    time.sleep(3)
    
    # Close popup if it appears
    try:
        close_button = driver.find_element(By.XPATH, "//button[contains(@class, '_2KpZ6l _2doB4z')]")
        close_button.click()
        print("Closed popup")
    except:
        print("No popup found")
    
    time.sleep(2)

# def login_with_mobile():
#     """Login to Flipkart using mobile number"""
#     global driver
#     print("\n--- Starting Login Process ---")
    
#     # Click on Login button
#     try:
#         login_button = driver.find_element(By.XPATH, "//a[text()='Login']")
#         login_button.click()
#         print("Clicked on Login button")
#         time.sleep(3)
#     except:
#         print("Login button not found, might already be on login page")
    
#     # Enter mobile number
#     mobile_number = input("9740557193")
    
#     try:
#         popup_container = driver.find_element(By.XPATH, "//div[contains(@class, 'contaiSm1-5F col col-3-5ner')]")  
#         driver.switch_to.frame(popup_container)
#         mobile_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter Mobile number']")
#         mobile_input.clear()
#         mobile_input.send_keys(mobile_number)
#         print(f"Entered mobile number: {mobile_number}")
#         time.sleep(2)
#     except:
#         print("Could not find mobile input field")
#         return False
    
#     # Click Request OTP button
#     try:
#         otp_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Request OTP')]")
#         otp_button.click()
#         print("Clicked Request OTP button")
#         time.sleep(5)
#     except:
#         print("Could not find Request OTP button")
#         return False
    
#     # Enter OTP
#     otp = input("Enter the OTP received on your mobile: ")
    
#     try:
#         otp_input = driver.find_element(By.XPATH, "//input[@maxlength='6']")
#         otp_input.send_keys(otp)
#         print("Entered OTP")
#         time.sleep(2)
#     except:
#         print("Could not find OTP input field")
#         return False
    
#     # Click Verify button
#     try:
#         verify_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Verify')]")
#         verify_button.click()
#         print("Clicked Verify button")
#         time.sleep(5)
#     except:
#         print("Could not find Verify button")
#         return False
    
#     print("Login completed successfully!")
#     return True

def search_for_laptops():
    """Search for laptops on Flipkart"""
    global driver
    print("\n--- Searching for Laptops ---")
    
    try:
        # Find search box
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys("laptops")
        search_box.send_keys(Keys.ENTER)
        print("Searched for laptops")
        time.sleep(5)
        return True
    except:
        print("Could not find search box")
        return False

def select_first_laptop():
    """Click on the first laptop in search results"""
    global driver
    print("\n--- Selecting First Laptop ---")
    
    try:
        # Find first laptop link
        first_laptop = driver.find_element(By.XPATH, "//div[@data-id][1]//a")
        first_laptop.click()
        print("Clicked on first laptop")
        time.sleep(5)
        
        # If new tab opened, switch to it
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])
            print("Switched to product page")
        
        return True
    except:
        print("Could not find or click on first laptop")
        return False

def add_to_cart():
    """Add the laptop to cart"""
    global driver
    print("\n--- Adding Laptop to Cart ---")
    
    try:
        # Find and click Add to Cart button
        add_cart_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add to cart')]")
        add_cart_button.click()
        print("Added laptop to cart")
        time.sleep(3)
        return True
    except:
        print("Could not find Add to Cart button")
        return False

def go_to_cart():
    """Navigate to shopping cart"""
    global driver
    print("\n--- Going to Cart ---")
    
    try:
        # Find and click cart icon
        cart_icon = driver.find_element(By.XPATH, "//a[contains(@href, '/viewcart')]")
        cart_icon.click()
        print("Opened cart")
        time.sleep(5)
        return True
    except:
        print("Could not find cart icon")
        return False

def proceed_to_checkout():
    """Proceed to checkout from cart"""
    global driver
    print("\n--- Proceeding to Checkout ---")
    
    try:
        # Find and click Place Order button
        place_order_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Place Order')]")
        place_order_button.click()
        print("Proceeded to checkout")
        time.sleep(5)
        return True
    except:
        print("Could not find Place Order button")
        return False

def complete_checkout():
    """Complete the checkout process"""
    print("\n--- Checkout Process ---")    
    # Let user see the checkout page
    input("Press Enter when you want to close the browser...")

def close_browser():
    """Close the browser"""
    global driver
    try:
        if driver:
            driver.quit()
            print("Browser closed")
    except:
        print("Browser was already closed")

def main():
    """Main function that runs the complete shopping process"""
    
    try:
        # Step 1: Setup browser
        setup_browser()
        
        # Step 2: Open Flipkart
        open_flipkart()
        
        # Step 3: Login
        # if not login_with_mobile():
        #     print("Login failed. Stopping here.")
        #     close_browser()
        #     return
        
        # Step 4: Search for laptops
        if not search_for_laptops():
            print("Search failed. Stopping here.")
            close_browser()
            return
        
        # Step 5: Select first laptop
        if not select_first_laptop():
            print("Could not select laptop. Stopping here.")
            close_browser()
            return
        
        # Step 6: Add to cart
        if not add_to_cart():
            print("Could not add to cart. Stopping here.")
            close_browser()
            return
        
        # Step 7: Go to cart
        if not go_to_cart():
            print("Could not open cart. Stopping here.")
            close_browser()
            return
        
        # Step 8: Proceed to checkout
        if not proceed_to_checkout():
            print("Could not proceed to checkout. Stopping here.")
            close_browser()
            return
        
        # Step 9: Complete checkout (manual)
        complete_checkout()
        
        print("\nAutomation completed successfully!")
        
    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        close_browser()

# Run the script
if __name__ == "__main__":
    print("IMPORTANT NOTES:")
    main()
   