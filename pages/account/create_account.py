from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage


class CreateAccountPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/create/"

    FIRST_NAME = (By.CSS_SELECTOR, "input#firstname")
    LAST_NAME = (By.CSS_SELECTOR, "input#lastname")
    EMAIL = (By.CSS_SELECTOR, "input#email_address")
    PASSWORD = (By.CSS_SELECTOR, "input#password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input#password-confirmation")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, "button.action.submit.primary")
    SUCCESS = "Thank you for registering with Main Website Store."
    ERROR = ("There is already an account with this email address. If you are sure that it is your email address, "
             "click here to get your password and access your account.")

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        self.current_url = url
        self.is_visible = self.visible
        self.is_clickable = self.clickable

    @property
    def first_name(self):
        return self.is_visible(self.FIRST_NAME)

    @first_name.setter
    def first_name(self, val: str):
        self.clear_and_send_keys(self.first_name, val)

    @property
    def last_name(self):
        return self.is_visible(self.LAST_NAME)

    @last_name.setter
    def last_name(self, val: str):
        self.clear_and_send_keys(self.last_name, val)

    @property
    def email(self):
        return self.is_visible(self.EMAIL)

    @email.setter
    def email(self, val: str):
        self.clear_and_send_keys(self.email, val)

    @property
    def password_one(self):
        return self.is_visible(self.PASSWORD)

    @password_one.setter
    def password_one(self, val: str):
        self.clear_and_send_keys(self.password_one, val)

    @property
    def password_two(self):
        return self.is_visible(self.PASSWORD_CONFIRM)

    @password_two.setter
    def password_two(self, val: str):
        self.clear_and_send_keys(self.password_two, val)

    def create_account(self):
        return self.is_visible(self.CREATE_ACCOUNT)

    def new(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_one = password
        self.password_two = password
        self.create_account().click()
        return self

    def element_label(self, locator):
        label = self.is_visible(locator).text
        script = "return window.getComputedStyle(document.querySelector('" + locator[
            1] + "'),'::after').getPropertyValue('content')"
        element = self.driver.execute_script(script)
        return label + ' ' + element.strip('"')

    def element_hint(self, locator):
        return self.is_visible(locator).get_attribute("title")




