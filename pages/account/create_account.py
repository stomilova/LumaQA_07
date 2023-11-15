from faker import Faker
from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage
from pages.account.my_account import MyAccountPage


class CreateAccountPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/create/"

    FIRST_NAME = (By.CSS_SELECTOR, "input#firstname")
    LAST_NAME = (By.CSS_SELECTOR, "input#lastname")
    EMAIL = (By.CSS_SELECTOR, "input#email_address")
    PASSWORD = (By.CSS_SELECTOR, "input#password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input#password-confirmation")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, "button.action.submit.primary")
    SUCCESS = "Thank you for registering with Main Website Store."
    ERROR_EMAIL_IN_USE = ("There is already an account with this email address. If you are sure that it is your"
                          " email address, click here to get your password and access your account.")

    def __init__(self, driver, url=URL, create=True, first_name=None, last_name=None, email=None, password=None):
        super().__init__(driver, url)
        self.current_url = url
        self.is_visible = self.visible
        self.is_clickable = self.clickable

        self.email_any = email is None

        self.first_name = first_name if first_name else Faker().first_name()
        self.last_name = last_name if last_name else Faker().last_name()
        self.email = email if email else Faker().email()
        self.password = password if password else Faker().password()
        if create:
            self.create_account()

    @property
    def first_name_i(self):
        return self.is_visible(self.FIRST_NAME)

    @first_name_i.setter
    def first_name_i(self, val: str):
        self.clear_and_send_keys(self.first_name_i, val)

    @property
    def last_name_i(self):
        return self.is_visible(self.LAST_NAME)

    @last_name_i.setter
    def last_name_i(self, val: str):
        self.clear_and_send_keys(self.last_name_i, val)

    @property
    def email_i(self):
        return self.is_visible(self.EMAIL)

    @email_i.setter
    def email_i(self, val: str):
        self.clear_and_send_keys(self.email_i, val)

    @property
    def password_one_i(self):
        return self.is_visible(self.PASSWORD)

    @password_one_i.setter
    def password_one_i(self, val: str):
        self.clear_and_send_keys(self.password_one_i, val)

    @property
    def password_two_i(self):
        return self.is_visible(self.PASSWORD_CONFIRM)

    @password_two_i.setter
    def password_two_i(self, val: str):
        self.clear_and_send_keys(self.password_two_i, val)

    def create_account_b(self):
        return self.is_visible(self.CREATE_ACCOUNT)

    def create_account(self):
        self.first_name_i = self.first_name
        self.last_name_i = self.last_name
        self.email_i = self.email
        self.password_one_i = self.password
        self.password_two_i = self.password
        self.create_account_b().click()
        if self.email_any:
            count = BasePage.ATTEMPTS
            while self.message == self.ERROR_EMAIL_IN_USE and count:
                self.email = Faker().email()
                self.email_i = self.email
                self.password_one_i = self.password
                self.password_two_i = self.password
                self.create_account_b().click()
                count -= 1
            assert self.message == self.SUCCESS, (f"Не удалось создать аккаунт c рандомным email"
                                                  f" за {BasePage.ATTEMPTS} попыток!")

    def element_label(self, locator):
        label = self.is_visible(locator).text
        script = ("return window.getComputedStyle(document.querySelector('" +
                  locator[1] + "'),'::after').getPropertyValue('content')")
        element = self.driver.execute_script(script)
        return label + ' ' + element.strip('"')

    def element_hint(self, locator):
        return self.is_visible(locator).get_attribute("title")
