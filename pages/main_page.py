from base.seleniumbase import BasePage
from locators.base_page_locators import BasePageLocators


class MainPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/'

    def check_visability_the_title(self):
        return self.is_visible(BasePageLocators.LOGO_TITLE)
