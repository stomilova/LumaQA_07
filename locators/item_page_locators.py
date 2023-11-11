from selenium.webdriver.common.by import By


class ItemPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='product-addtocart-button']")

    QUANTITY_OF_ITEM = (By.XPATH, "//*[@id='qty']")
    QUANTITY_ERROR_MSG = (By.XPATH, "//*[@id='qty-error']")

    # Clamber Watch Locators
    LINK_CLAMBER_WATCH = (
        By.XPATH, "//div/a[@href='https://magento.softwaretestingboard.com/clamber-watch.html']")
    ADD_TO_CART_CLAMBER_WATCH_BUTTON = (By.XPATH, "//input[@value='43']/following-sibling::button")

