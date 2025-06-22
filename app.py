'''
# Improved Flipkart Automation Script - maintains original structure
# This script automates search, add to cart, and checkout on Flipkart
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selectors_config as FlipkartSelectors

# Global variable to store our browser
driver = None  # Initialize driver as None

def setup_browser():
    """Setup and open Chrome browser"""
    global driver  # Declare global here
    print("Setting up browser...")
    # Create Chrome browser instance
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    print("Browser ready!")

def open_flipkart():
    """Open Flipkart website"""
    print("Opening Flipkart...")
    driver.get(FlipkartSelectors.URL_HOME)
    
    # Close popup if it appears
    try:
        close_button = driver.find_element(By.XPATH, FlipkartSelectors.POPUP_CLOSE_BUTTON)
        close_button.click()
    except:
        pass

def search_for_laptops():
    """Search for laptops on Flipkart"""
    print("Searching for laptops...")
    
    try:
        search_box = driver.find_element(By.NAME, FlipkartSelectors.SEARCH_BOX_NAME)
        search_box.clear()
        search_box.send_keys(FlipkartSelectors.SEARCH)
        search_box.send_keys(Keys.ENTER)
        return True
    except:
        return False

def select_second_laptop():
    """Click on the second laptop in search results"""
    print("Selecting second laptop...")
    
    try:
        # First try to get all laptops and select the second one
        laptops = driver.find_elements(By.XPATH, FlipkartSelectors.ALL_LAPTOPS_XPATH)
        if len(laptops) >= 2:
            second_laptop = laptops[1]  # Index 1 for second laptop
            second_laptop.click()
        else:
            # Fallback to direct second laptop selector
            second_laptop = driver.find_element(By.XPATH, FlipkartSelectors.SECOND_LAPTOP_XPATH_ALT)
            second_laptop.click()
        # If new tab opened, switch to it
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])
        return True
    except:
        return False

def add_to_cart():
    """Add the laptop to cart"""
    print("Adding to cart...")
    
    try:
        add_cart_button = driver.find_element(By.XPATH, FlipkartSelectors.ADD_TO_CART_BUTTON)
        add_cart_button.click()
        return True
    except:
        return False

def go_to_cart():
    """Navigate to shopping cart"""
    print("Going to cart...")
    
    try:
        cart_icon = driver.find_element(By.XPATH, FlipkartSelectors.CART_ICON)
        cart_icon.click()
        return True
    except:
        return False

def proceed_to_checkout():
    """Proceed to checkout from cart"""
    print("Proceeding to checkout...")
    
    try:
        place_order_button = driver.find_element(By.XPATH, FlipkartSelectors.PLACE_ORDER_BUTTON)
        place_order_button.click()
        return True
    except:
        return False

def complete_checkout():
    """Complete the checkout process"""
    print("Manual checkout required from here...")
    input("Press Enter when you want to close the browser...")

def close_browser():
    """Close the browser"""
    try:
        if driver:
            driver.quit()
            print("Browser closed")
    except:
        pass

def main():
    """Main function that runs the complete shopping process"""
    try:
        setup_browser()
        open_flipkart() 
        # Login is optional - uncomment if needed
        # if not login_with_mobile():
        #     print("Login failed. Continuing without login...")  
        if not search_for_laptops():
            print("Search failed.")
            close_browser()
            return
        
        if not select_second_laptop():
            print("Could not select second laptop.")
            close_browser()
            return
        
        if not add_to_cart():
            print("Could not add to cart.")
            close_browser()
            return
        
        if not go_to_cart():
            print("Could not open cart.")
            close_browser()
            return
        
        if not proceed_to_checkout():
            print("Could not proceed to checkout.")
            close_browser()
            return 
        complete_checkout()
        print("Automation completed successfully!")
        
    except KeyboardInterrupt:
        print("Stopped by user")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        close_browser()

# Run the script
if __name__ == "__main__":
    print("FLIPKART AUTOMATION SCRIPT - SELECTS 2ND LAPTOP")
    main()