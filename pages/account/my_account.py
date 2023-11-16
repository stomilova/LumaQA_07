from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage


class MyAccountPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/"

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        self.current_url = url

