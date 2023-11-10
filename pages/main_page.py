from base.seleniumbase import BasePage
from locators.base_page_locators import BasePageLocators
from locators.item_page_locators import ItemPageLocators


class MainPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/'

    def check_visibility_the_title(self):
        return self.is_visible(BasePageLocators.LOGO_TITLE)

    def check_visibility_of_erin_recommends_widget(self):
        return self.is_visible(BasePageLocators.ERIN_SECTION)

    def add_clamber_watch_from_gear_catalog_to_cart(self):
        self.hold_mouse_on_element(BasePageLocators.LINK_GEAR_CATALOG)
        self.is_clickable(BasePageLocators.LINK_WATCHES_CATALOG).click()
        self.hold_mouse_on_element(ItemPageLocators.LINK_CLAMBER_WATCH)
        self.is_clickable(ItemPageLocators.ADD_TO_CART_CLAMBER_WATCH_BUTTON).click()
        self.is_visible(BasePageLocators.MSG_SUCCESS)