from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import BasePage

class OrderAndPaymentPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/sales/guest/form/"

    # def order_id_field(self) -> WebElement:
    #     return self.is_visible(OrdersAndReturnsPageLocators.ORDER_ID_FIELD)