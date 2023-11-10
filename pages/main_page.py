from base.seleniumbase import BasePage
from locators.base_page_locators import BasePageLocators


class MainPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/'

    def check_visibility_the_title(self):
        return self.is_visible(BasePageLocators.LOGO_TITLE)

    def check_visibility_of_erin_recommends_widget(self):
        return self.is_visible(BasePageLocators.ERIN_SECTION)

    def check_clickability_of_erin_recommends_widget(self):
        return self.is_clickable(BasePageLocators.ERIN_SECTION)
