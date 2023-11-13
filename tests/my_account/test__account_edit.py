from data.fake_data import FakeData
from pages.account.account_edit import AccountEditPage
from pages.account.my_account import MyAccountPage
from pages.account.sign_in import SignInPage


class TestX(FakeData):
    def test_change_first_name(self, driver, create_account):
        page = AccountEditPage(driver)
        page.first_name = self.first_name
        page.save().click()
        assert page.current_url == MyAccountPage.URL, "Unexpected page URL"
        assert page.message_success == AccountEditPage.SUCCESS, "Message not as expected"

    def test_change_last_name(self, driver, create_account):
        page = AccountEditPage(driver)
        page.last_name = self.last_name
        page.save().click()
        assert page.current_url == MyAccountPage.URL, "Unexpected page URL"
        assert page.message_success == AccountEditPage.SUCCESS, "Message not as expected"

    def test_change_email(self, driver, create_account, password):
        page = AccountEditPage(driver)
        page.change_email().click()
        page.email = self.email
        page.password_current = password
        page.save().click()
        assert page.current_url == SignInPage.URL, "Unexpected page URL"
        assert page.message_success == AccountEditPage.SUCCESS, "Message not as expected"

    def test_change_password(self, driver, create_account, password):
        page = AccountEditPage(driver)
        page.change_password().click()
        page.password_current = password
        page.password = (password_new := self.password)
        page.password_confirm = password_new
        page.save().click()
        assert page.current_url == SignInPage.URL, "Unexpected page URL"
        assert page.message_success == AccountEditPage.SUCCESS, "Message not as expected"

    def test_change_email_and_password(self, driver, create_account, password):
        page = AccountEditPage(driver)
        page.change_email().click()
        page.change_password().click()
        page.email = self.email
        page.password_current = password
        page.password = (password_new := self.password)
        page.password_confirm = password_new
        page.save().click()
        assert page.current_url == SignInPage.URL, "Unexpected page URL"
        assert page.message_success == AccountEditPage.SUCCESS, "Message not as expected"
