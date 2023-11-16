from selenium.webdriver.common.by import By


class MyAccountPageLocators:
    MY_ACCOUNT_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[1]")
    MY_ORDERS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[2]")
    MY_DOWNLOADABLE_PRODUCTS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[3]")
    MY_WISH_LIST_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[4]")
    ADDRESS_BOOK_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[6]")
    ACCOUNT_INFORMATION_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[7]")
    STORED_PAYMENT_METHODS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[8]")
    MY_PRODUCT_REVIEWS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[10]")