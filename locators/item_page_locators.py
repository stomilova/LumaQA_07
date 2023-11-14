from selenium.webdriver.common.by import By


class ItemPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='product-addtocart-button']")

    ADD_YOUR_REVIEW_LINK = (By.XPATH,"//*[@class='action add']")
    BLOCK_REVIEW_ADD = (By.XPATH,"//*[@class='block review-add']")
    ITEM_REVIEW_COUNT = (By.XPATH, "//span[@itemprop='reviewCount']")
    ITEM_REVIEW_LINK = (By.XPATH, "//*[text()='Reviews']")
    ITEM_RATING = (By.XPATH, "//div[@class='rating-summary']//div[@class='rating-result']")

    CUSTOMER_REVIEWS_HEADER = (By.XPATH, "//strong[text() = 'Customer Reviews']")

    QUANTITY_OF_ITEM = (By.XPATH, "//*[@id='qty']")
    QUANTITY_ERROR_MSG = (By.XPATH, "//*[@id='qty-error']")

    # Clamber Watch Locators
    LINK_CLAMBER_WATCH = (
        By.XPATH, "//div/a[@href='https://magento.softwaretestingboard.com/clamber-watch.html']")
    ADD_TO_CART_CLAMBER_WATCH_BUTTON = (By.XPATH, "//input[@value='43']/following-sibling::button")
