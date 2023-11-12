from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage
# from urllib import parse
# from base64 import b64decode


class SignInPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/login/"
    EMAIL = (By.CSS_SELECTOR, "input#email")
    PASSWORD = (By.CSS_SELECTOR, "input#pass")
    SIGN_IN = (By.CSS_SELECTOR, "button.action.login.primary")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "a.action.remind")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, "a.action.create.primary")

    ERROR = "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        self.current_url = url

        # self.referer = parse.unquote(url.split('referer/')[1])
        # print(b64decode(self.referer))

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
    def password_one(self,  val: str) -> None:
        self.clear_and_send_keys(self.password_one, val)

    def sign_in(self):
        return self.is_visible(self.SIGN_IN)

    def forgot_password(self):
        return self.is_visible(self.FORGOT_PASSWORD)

    def create_account(self):
        return self.is_visible(self.CREATE_ACCOUNT)


class ForgotPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/forgotpassword/"
    URL_DONE = "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw%2C%2C/"

    EMAIL = (By.CSS_SELECTOR, "input#email_address")
    RESET_PASSWORD = (By.CSS_SELECTOR, "button.action.submit.primary")

    SUCCESS = "If there is an account associated with %s you will receive an email with a link to reset your password."

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        self.current_url = url

    @property
    def email(self):
        return self.is_visible(self.EMAIL)

    @email.setter
    def email(self, val: str):
        self.clear_and_send_keys(self.email, val)

    def reset_password(self):
        return self.is_visible(self.RESET_PASSWORD)
