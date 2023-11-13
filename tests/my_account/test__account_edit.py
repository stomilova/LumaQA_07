from random import choice

from data.fake_data import FakeData
from pages.account.account_add_address import AddressAddPage
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

    def test_add_address_with_select_state(self, driver, create_account):
        page = AddressAddPage(driver)
        page.company = self.company
        page.telephone = self.phone_number

        page.country = choice(AddressAddPage.WITH_REGIONS)
        page.state = (state := choice(page.state[1:]))
        page.city = (city := self.city)
        page.postcode = (postcode := self.postcode)
        page.street_1 = self.secondary_address
        page.street_2 = self.street_address
        page.street_3 = f"{city} {state} {postcode}"

        # page.set_billing.click()
        page.save().click()

        assert page.current_url == AddressAddPage.URL_DONE
        assert page.message_success == AddressAddPage.SUCCESS

    def test_add_address_with_input_state(self, driver, create_account):
        page = AddressAddPage(driver)
        page.company = self.company
        page.telephone = self.phone_number

        page.country = choice(list(filter(lambda x: x not in AddressAddPage.WITH_REGIONS, page.country)))

        city = self.city
        state = self.state
        postcode = self.postcode
        page.street_1 = self.secondary_address
        page.street_2 = self.street_address
        page.street_3 = f"{city} {state} {postcode}"
        page.city = city
        page.postcode = postcode
        page.region = state

        # page.set_shpping.click()

        page.save().click()

        assert page.current_url == AddressAddPage.URL_DONE
        assert page.message_success == AddressAddPage.SUCCESS
