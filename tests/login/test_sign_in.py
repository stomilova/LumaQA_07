from locators.login_page_locators import LoginPageLocators
from pages.login.login_page import LoginPage


def test_sign_in(driver):
    page = LoginPage(driver, LoginPageLocators.URL)
    page.open()
    page.sign_in()
    assert page.header().text == 'My Account', 'Не удалось войти'

