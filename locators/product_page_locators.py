from selenium.webdriver.common.by import By

class ProductPageLocators:

    # Product page
    HEADER = (By.XPATH, "//header[@class='page-header']")
    NAVIGATION_SECTION = (By.XPATH, "//div[@class='sections nav-sections']")
    BREADCRUMBS = (By.XPATH, "//div[@class='breadcrumbs']")
    BODY = (By.XPATH, "//main[@id='maincontent']")
    FOOTER = (By.XPATH, "//footer[@class='page-footer']")
    COPYRIGHT = (By.XPATH, "//small[@class='copyright']")

    # class="product-info-main"
    PRODUCT_NAME = (By.XPATH, "//span[@itemprop='name']")

    # class="product media"

    # class="product info detailed"


    # class="block upsell"

