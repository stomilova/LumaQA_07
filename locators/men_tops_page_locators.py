from selenium.webdriver.common.by import By


class MenTopsPageLocators:
    TOP_MEN_PRODUCT_FOTO = (
        By.CSS_SELECTOR, "a[class='product photo product-item-photo'] img[alt='Cassius Sparring Tank']")
    TOP_MEN_PRODUCT_TITLE = (
        By.XPATH, "//div[@class = 'product details product-item-details']//a[contains(text(), 'Cassius')]")

    # PAGE_NAME = (By.TAG_NAME, "h1")

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
    def location_product_item(position: int):
        return By.CSS_SELECTOR, f"li[class='item product product-item']:nth-child({position})"
