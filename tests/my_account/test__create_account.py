import pytest

from data.fake_data import FakeData
from locators.create_new_account_locators import CreateNewAccountPageLocators as Label
from pages.account.create_account import CreateAccountPage
from pages.account.my_account import MyAccountPage
from pages.login.logout_page import LogoutPage
from pages.main_page import MainPage


class TestX(FakeData):
    def test_create_account(self, driver):
        page = CreateAccountPage(driver)
        assert page.current_url == MyAccountPage.URL, "User is not on expected page"
        assert page.message_success == CreateAccountPage.SUCCESS, "Success message not as expected"

    def test_create_second_account_with_same_email(self, driver):
        page = CreateAccountPage(driver)
        LogoutPage(driver)
        page = CreateAccountPage(driver, email=page.email)
        assert page.current_url == CreateAccountPage.URL, "User is not on expected page"
        assert page.message_error == CreateAccountPage.ERROR_EMAIL_IN_USE, "Message not as expected"

    def test_logout(self, driver, create_account):
        page = LogoutPage(driver)
        assert page.current_url == LogoutPage.URL_SUCCESS, "User is not on expected page"
        page.redirect(MainPage.URL, 6)
        assert page.current_url == MainPage.URL, "User not redirected to expected page"

    @pytest.mark.parametrize('locator, expected', [(Label.FIRST_NAME_LABEL, 'First Name *'),
                                                   (Label.LAST_NAME_LABEL, 'Last Name *'),
                                                   (Label.EMAIL_LABEL, 'Email *'),
                                                   (Label.PASSWORD_LABEL, 'Password *'),
                                                   (Label.CONFIRM_PASSWORD_LABEL, 'Confirm Password *')])
    def test_account_form_label(self, driver, locator, expected):
        page = CreateAccountPage(driver, create=False)
        assert page.element_label(locator) == expected, f'У поля {expected[:-2]} нету *'

    @pytest.mark.parametrize('locator, expected', [(Label.FIRST_NAME_FIELD, 'First Name'),
                                                   (Label.LAST_NAME_FIELD, 'Last Name'),
                                                   (Label.EMAIL_FIELD, 'Email'),
                                                   (Label.PASSWORD_FIELD, 'Password'),
                                                   (Label.CONFIRM_PASSWORD_FIELD, 'Confirm Password')])
    def test_account_form_hints(self, driver, locator, expected):
        page = CreateAccountPage(driver, create=False)
        assert page.element_hint(locator) == expected, f'У поля {expected} нету хинта'
