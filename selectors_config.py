# selectors_config.py
# ==================== POPUP AND MODAL SELECTORS ====================
POPUP_CLOSE_BUTTON = "//button[text()='✕']"
URL_HOME = "https://www.flipkart.com"
SEARCH = "laptops"
SEARCH_BOX_NAME = "q"
SEARCH_BOX_XPATH = "//input[@name='q']"

# ==================== PRODUCT LISTING SELECTORS ====================

ALL_LAPTOPS_XPATH = "//div[@data-id]//a[contains(@href, '/p/')]"

# Direct second laptop selectors
SECOND_LAPTOP_XPATH = "(//div[@data-id]//a[contains(@href, '/p/')])[2]"
SECOND_LAPTOP_XPATH_ALT = "(//div[@data-id])[2]//a"
ADD_TO_CART_BUTTON = "//li[@class='col col-6-12']//button[contains(@class, 'In9uk2')]"
BUY_NOW_BUTTON = "//button[contains(text(), 'Buy Now')]"
BUY_NOW_BUTTON_ALT = "//button[contains(text(), 'BUY NOW')]"
CART_ICON = "//a[contains(@href, '/viewcart')]"

# ==================== CHECKOUT SELECTORS ====================
PLACE_ORDER_BUTTON = "//button[contains(text(), 'Place Order')]"
PROCEED_TO_PAY_BUTTON = "//button[contains(text(), 'Proceed to Pay')]"

