from selenium.webdriver.common.by import By


class SalePageLocators:
    SHOP_WOMENS_DEALS = (By.XPATH, '//*[contains(text(), "Shop Women’s Deals")]')
    SHOP_MENS_DEALS = (By.XPATH, '//span[contains(text(), "Shop Men’s Deals")]')
    SHOP_LUMA_GEAR = (By.XPATH, '//*[contains(text(), "Shop Luma Gear")]')
    TEES_ON_SALE = (By.XPATH, '//*[contains(text(), "Tees on sale")]')
    PRODUCTS_LIST = (By.XPATH, '//ol[@class="products list items product-items"]')
    BASKET = (By.CSS_SELECTOR, 'a[class="action showcart"]')
    ADD_TO_CARD = (By.XPATH, '//button[@id="product-addtocart-button"] ')
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, 'div button[id="top-cart-btn-checkout"]')


class ItemsLocators:
    ITEMS_LIST = (By.CSS_SELECTOR, 'div[class="product details product-item-details"]')
