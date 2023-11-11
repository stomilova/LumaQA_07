from base.seleniumbase import BasePage


class LogoutPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/logout/"
    URL_SUCCESS = "https://magento.softwaretestingboard.com/customer/account/logoutSuccess/"

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        self.current_url = url
