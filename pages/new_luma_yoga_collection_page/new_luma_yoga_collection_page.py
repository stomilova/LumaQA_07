from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage
from locators.new_luma_yoga_collection_locators.PriceTabLocators import PRICE_TAB
from selenium.webdriver.remote.webelement import WebElement
#PRICE_TAB,PRICE_LIST,PRICE_LEVEL_LOCATOR



class NewLumaYogaCollectionPage(BasePage):
    # page with categories

    def __init__(self, driver):
        super().__init__(
            url='https://magento.softwaretestingboard.com/collections/yoga-new.html',
            driver=driver
        )
    def find_price_tab_and_click(self) -> WebElement:
        return self.is_clickable(locator=PriceTabLocators.PRICE_TAB).click()

    def find_element_in_sidebar(self, locator: tuple) -> WebElement:
        sidebar = self.find_sidebar()
        return self.find_visible_element_in_sidebar(sidebar, *locator)

    def find_elements_in_price_tab(self, locator: tuple) -> list[WebElement]:
        sidebar = self.find_sidebar()
        return self.find_visible_elements_in_price_tab(sidebar, locator)

    def find_visible_elements_price_tab(
        self, sidebar: WebElement, locator: tuple
    ) -> list[WebElement]:
        return sidebar.find_elements(*locator)


    # def rederect_to_the_current_category_page(
    #     self, category: WebElement, category_url: str
    # ) -> WebElement:
    #     category.click()
    #     self.redirect(url=category_url)
    #     return category_page.CategoryPage(driver=self.driver, url=category_url)