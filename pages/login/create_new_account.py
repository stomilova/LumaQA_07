from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import BasePage
from locators.base_page_locators import BasePageLocators
from locators.create_new_account_locators import CreateNewAccountPageLocators


class CreateNewAccountPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/create"

    def first_name_field(self) -> WebElement:
        return self.is_visible(CreateNewAccountPageLocators.FIRST_NAME_FIELD)

    def last_name_field(self) -> WebElement:
        return self.is_visible(CreateNewAccountPageLocators.LAST_NAME_FIELD)

    def email_field(self) -> WebElement:
        return self.is_visible(CreateNewAccountPageLocators.EMAIL_FIELD)

    def first_password_field(self) -> WebElement:
        return self.is_visible(CreateNewAccountPageLocators.PASSWORD_FIELD)

    def confirm_password_field(self) -> WebElement:
        return self.is_visible(CreateNewAccountPageLocators.CONFIRM_PASSWORD_FIELD)

    def create_new_account_button(self) -> WebElement:
        return self.is_clickable(CreateNewAccountPageLocators.CREATE_ACCOUNT_BUTTON)

    def success_create_account_msg(self) -> WebElement:
        return self.is_visible(BasePageLocators.MSG_SUCCESS)

    def fill_in_all_required_fields(self, firstname, lastname, email, password):
        self.clear_and_send_keys(self.first_name_field(), firstname)
        self.clear_and_send_keys(self.last_name_field(), lastname)
        self.clear_and_send_keys(self.email_field(), email)
        self.clear_and_send_keys(self.first_password_field(), password)
        self.clear_and_send_keys(self.confirm_password_field(), password)

    def create_new_account(self, firstname, lastname, email, password):
        self.fill_in_all_required_fields(firstname, lastname, email, password)
        self.create_new_account_button().click()
