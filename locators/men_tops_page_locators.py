from selenium.webdriver.common.by import By


class MenTopsPageLocators:
    TOP_MEN_PRODUCT_FOTO = (By.CSS_SELECTOR,
                            "a[class='product photo product-item-photo'] img[alt='Cassius Sparring Tank']")
    TOP_MEN_PRODUCT_TITLE = (By.XPATH,
                             "//div[@class = 'product details product-item-details']//a[contains(text(), 'Cassius')]")
    TOP_MEN_SORTER = (By.CSS_SELECTOR, '.toolbar-products:nth-child(4) .sorter-options')
    TOP_MEN_PRODUCT_ITEMS_NAME = (By.CSS_SELECTOR, '.product-items .product-item-link')
    TOP_MEN_ARROW = (By.CSS_SELECTOR, ".toolbar-products:nth-child(4) .sort-asc")
    TOP_MEN_PRODUCT_ITEMS_PRICE = (By.CSS_SELECTOR, ".price-wrapper .price")
    TOP_MEN_LIST_MODE = (By.CSS_SELECTOR, ".toolbar-products:nth-child(4) .mode-list")
    SHOPING_OPTIONS_MENU = (By.CSS_SELECTOR, '#narrow-by-list div.filter-options-title')

    WISH_LIST_ITEM = [(1, (By.XPATH, "//li[@class='product-item']//a[@title='Cassius Sparring Tank']")),
                      (2, (By.XPATH, "//li[@class='product-item']//a[@title='Atlas Fitness Tank']")),
                      (3, (By.XPATH, "//li[@class='product-item']//a[@title='Tiberius Gym Tank']")),
                      (4, (By.XPATH, "//li[@class='product-item']//a[@title='Sinbad Fitness Tank']"))]
    @staticmethod
    def get_product_trough_foto(position: int):
        return By.CSS_SELECTOR, f"li[class='item product product-item']:nth-child({position}) img[class='product-image-photo']"

    @staticmethod
    def get_product_trough_title(position: int):
        return By.CSS_SELECTOR, f"li[class='item product product-item']:nth-child({position}) a[class='product-item-link']"

    @staticmethod
    def location_add_button(position: int):
        return By.CSS_SELECTOR, f"li[class='item product product-item']:nth-child({position}) button"

    @staticmethod
    def location_heart_shaped_button(position: int):
        return By.CSS_SELECTOR, f"li[class='item product product-item']:nth-child({position}) a[class='action towishlist']"

    @staticmethod
    def location_product_item(position: int):
        return By.CSS_SELECTOR, f"li[class='item product product-item']:nth-child({position})"
