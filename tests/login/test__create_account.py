from time import sleep
from data.fake_data import FakeData
from pages.account.create_account import CreateAccountPage
from pages.account.my_account import MyAccountPage
from pages.login.logout_page import LogoutPage
from pages.main_page import MainPage


class TestX(FakeData):
    def test_create_account(self, driver):
        page = CreateAccountPage(driver).new(self.first_name, self.last_name, self.email, self.password)
        assert page.current_url == MyAccountPage.URL
        assert page.message_success == CreateAccountPage.SUCCESS

    def test_create_second_account_with_same_email(self, driver, create_account, email):
        LogoutPage(driver)
        page = CreateAccountPage(driver).new(self.first_name, self.last_name, email, self.password)
        assert page.current_url == CreateAccountPage.URL
        assert page.message_error == CreateAccountPage.ERROR

    def test_logout(self, driver, create_account):
        page = LogoutPage(driver)
        assert page.current_url == LogoutPage.URL_SUCCESS
        sleep(6)
        assert page.current_url == MainPage.URL
