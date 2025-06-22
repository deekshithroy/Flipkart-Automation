# selectors_config.py
# Configuration file for robust XPath and CSS selectors for Flipkart automation
# Updated to avoid changing class names and use stable parent/root elements
# Simple variable-based approach without classes

# ==================== POPUP AND MODAL SELECTORS ====================
POPUP_CLOSE_BUTTON = "//button[text()='✕']"
URL_HOME = "https://www.flipkart.com"
SEARCH = "laptops"


# ==================== LOGIN RELATED SELECTORS ====================
LOGIN_BUTTON = "//a[contains(text(), 'Login')]"
# LOGIN_BUTTON_ALT = "//button[contains(text(), 'Login')]"
MOBILE_INPUT = "//input[contains(@placeholder, 'Enter Mobile number')]"
MOBILE_INPUT_ALT = "//input[@type='text' and contains(@maxlength, '10')]"
REQUEST_OTP_BUTTON = "//button[contains(text(), 'Request OTP')]"
REQUEST_OTP_BUTTON_ALT = "//button[contains(text(), 'SEND OTP')]"
OTP_INPUT = "//input[@maxlength='6']"
OTP_INPUT_ALT = "//input[contains(@placeholder, 'Enter OTP')]"
VERIFY_BUTTON = "//button[contains(text(), 'Verify')]"
VERIFY_BUTTON_ALT = "//button[contains(text(), 'VERIFY')]"

# ==================== SEARCH RELATED SELECTORS ====================
SEARCH_BOX_NAME = "q"
SEARCH_BOX_XPATH = "//input[@name='q']"

# ==================== PRODUCT LISTING SELECTORS ====================
# Get all laptop links - more reliable approach
ALL_LAPTOPS_XPATH = "//div[@data-id]//a[contains(@href, '/p/')]"

# Direct second laptop selectors
SECOND_LAPTOP_XPATH = "(//div[@data-id]//a[contains(@href, '/p/')])[2]"
SECOND_LAPTOP_XPATH_ALT = "(//div[@data-id])[2]//a"

# Product container selectors
PRODUCT_CONTAINERS = "//div[@data-id]"
PRODUCT_LINKS = "//div[@data-id]//a"

# ==================== PRODUCT PAGE SELECTORS ====================
ADD_TO_CART_BUTTON = "//li[@class='col col-6-12']//button[contains(@class, 'In9uk2')]"

BUY_NOW_BUTTON = "//button[contains(text(), 'Buy Now')]"
BUY_NOW_BUTTON_ALT = "//button[contains(text(), 'BUY NOW')]"

# ==================== CART RELATED SELECTORS ====================
CART_ICON = "//a[contains(@href, '/viewcart')]"


CART_COUNT = "//span[contains(text(), '1')]"
# CART_COUNT_ALT = "//a[contains(@href, 'cart')]//span"

# ==================== CHECKOUT SELECTORS ====================
PLACE_ORDER_BUTTON = "//button[contains(text(), 'Place Order')]"


PROCEED_TO_PAY_BUTTON = "//button[contains(text(), 'Proceed to Pay')]"
# PROCEED_TO_PAY_BUTTON_ALT = "//button[contains(text(), 'PROCEED TO PAY')]"

# ==================== STABLE SELECTORS USING STRUCTURE ====================
# Search selectors using form structure
SEARCH_FORM_INPUT = "//form//input[@name='q']"
SEARCH_HEADER_INPUT = "//header//input[@name='q']"

# Product selectors using main content area
MAIN_PRODUCTS = "//main//div[@data-id]"
CONTENT_PRODUCTS = "//div[@id='container']//div[@data-id]"

# Navigation selectors
NAV_CART = "//nav//a[contains(@href, 'cart')]"
HEADER_CART = "//header//a[contains(@href, 'cart')]"

# Button selectors using parent elements
BUTTON_PRIMARY = "//li//button[contains(text(), 'Add to cart')]"
FORM_BUTTON = "//form//button[@type='button']"


