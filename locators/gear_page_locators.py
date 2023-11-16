from selenium.webdriver.common.by import By

class GearPageLocators:
    # Categories on Gear page
    SIDEBAR_ELEMENTS = (By.XPATH,'//dd//a')
    SIDEBAR_MAIN = (By.XPATH,'//div[@class="sidebar sidebar-main"]')
    SHOP_BY_TITLE = (By.XPATH,'.//div[@class="title"]/strong')
    CATEGORY_TITLE = (By.XPATH,'//dl[@id="narrow-by-list2"]/dt')

class CategoryPageLocators:    
    # category page
    LAST_ITEM_COUNTER= (By.XPATH,'//p[@id="toolbar-amount"]//span[last()]')
    ITEM_ON_THE_PAGE = (By.XPATH,'//a[@class="product-item-link"]')
    NEXT_BUTTON = (By.XPATH,'//div[@class="pages"]//a[@class="action  next"][last()]')
