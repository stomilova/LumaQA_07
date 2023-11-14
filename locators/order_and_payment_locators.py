from selenium.webdriver.common.by import By


class OrdersAndPaymentPageLocators:
    """"Элементы до страницы заказа"""
    NEW_YOGA_BUTTON = (By.XPATH, "//span[contains(@class, 'content')]//span[contains(@class, 'button')]")
    ECHO_FIT_COMPRESSION_SHORT = (By.XPATH, "//div[@class='product-item-info']//a[contains(text(), 'Echo Fit Compression Short')]")
    SHOPPING_CART_BUTTON = (By.XPATH, "//a[contains(@class, 'showcart')]")
    PROCEED_TO_CHECKOUT = (By.XPATH, "//div[@class='primary']/button[@id='top-cart-btn-checkout']")

    """"Форма оформления заказа"""
    EMAIL_FIELD = (By.XPATH, "//fieldset[@class='fieldset']//input[@id='customer-email']")
    FIRST_NAME = (By.XPATH, "//div[@class='control']//input[@name='firstname']")
    LAST_NAME = (By.XPATH, "//div[@class='control']//input[@name='lastname']")
    STREET_ADDRESS_1 = (By.XPATH, "//div[@class='control']//input[@name='street[0]']")
    CITY = (By.XPATH, "//div[@class='control']//input[@name='city']")
    STATE_DROPDOWN = (By.XPATH, "//select[@name='region_id']")
    ALABAMA_OPTION = (By.XPATH, "//option[@data-title='Alabama']")
    POSTCODE = (By.XPATH, "//div[@class='control']//input[@name='postcode']")
    COUNTRY = (By.XPATH, "//select[@name='country_id']")
    UINTED_STATES_OPTION = (By.XPATH, "//option[@data-title='United States']")
    PHONE = (By.XPATH, "//div[contains(@class,  'control')]//input[@name='telephone']")

    """"Кнопки формы"""
    NEXT_BUTTON = (By.XPATH, "//div[@class='primary']//button[contains(@class, 'continue')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//div[@class='primary']//button[@title='Place Order']")



