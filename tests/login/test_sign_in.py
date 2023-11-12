from data.fake_data import FakeData
from locators.login_page_locators import LoginPageLocators
from pages.account.my_account import MyAccountPage
from pages.account.sign_in import SignInPage
from pages.login.login_page import LoginPage
from pages.login.logout_page import LogoutPage


def test_sign_in(driver):
    page = LoginPage(driver, LoginPageLocators.URL)
    page.open()
    page.sign_in()
    assert page.header().text == 'My Account', 'Не удалось войти'


class TestX(FakeData):
    def test_correct_credentials_login(self, driver, create_account, email, password):
        LogoutPage(driver)
        page = SignInPage(driver)
        page.email = email
        page.password_one = password
        page.sign_in().click()
        assert page.current_url == MyAccountPage.URL, "Login with correct credentials failed"

    def test_bad_credentials_login(self, driver, email, password):
        page = SignInPage(driver)
        page.email = email
        page.password_one = password
        page.sign_in().click()
        assert page.current_url == SignInPage.URL, "Unexpected page URL"
        assert page.message_error == SignInPage.ERROR, "Successful login with random credentials"
