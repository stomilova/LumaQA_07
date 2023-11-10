from data.fake_data import FakeData
from locators.orders_and_returns import OrdersAndReturnsPageLocators
from pages.footer.orders_and_returns import OrdersAndReturnsPage


class TestIncorrectEmailFill(FakeData):

    def test_email_without_dot(self, driver):
        """TC_012.009.001 | Footer > 'Orders and Returns' > Email incorrect format\n
        Pre-conditions:
            The user is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ )
            and user not logged into the account.
        Steps:
            User enters email in incorrect format in the 'Email' field and clicks the 'Continue' button
        Expected results:
            Under the 'Email' field, an error message appears:
            'Please enter a valid email address (Ex: johndoe@domain.com).' """
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_email(order_id=self.fake_order_id, email='dadqweq3@mailcom',
                                       billing_lastname=self.last_name)
        page.continue_button().click()
        assert page.error_msg_email_not_filled_or_incorrect_type().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_EMAIL_TYPE, "Не появилась ошибка про неправильный формат email"

    def test_email_without_at(self, driver):
        """TC_012.009.001 | Footer > 'Orders and Returns' > Email incorrect format\n
        Pre-conditions:
            The user is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ )
            and user not logged into the account.
        Steps:
            User enters email in incorrect format in the 'Email' field and clicks the 'Continue' button
        Expected results:
            Under the 'Email' field, an error message appears:
            'Please enter a valid email address (Ex: johndoe@domain.com).' """
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_email(order_id=self.fake_order_id, email='dadqweq3amail.com',
                                       billing_lastname=self.last_name)
        page.continue_button().click()
        assert page.error_msg_email_not_filled_or_incorrect_type().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_EMAIL_TYPE, "Не появилась ошибка про неправильный формат email"


class TestFieldsNotFilled(FakeData):
    def test_order_id_field_not_filled(self, driver):
        """TC_012.009.002 | Footer > “Orders and Returns” > Order_ID field\n
        Pre-conditions:
            The user is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ )
            and user not logged into the account.
        Steps:
            The user filled in all fields except 'Order_id' and clicks the "Continue" button
        Expected results:
            Error message 'This is a required field.' appeared under the "Order ID" field."""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_email(order_id='', email=self.email, billing_lastname=self.last_name)
        page.continue_button().click()
        assert page.error_msg_order_id_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле order_id не заполнено , а ошибка не показана"

    def test_billing_lastname_field_not_filled(self, driver):
        """TC_012.009.003 | Footer > “Orders and Returns” > Billing_Last_Name_field\n
        Pre-conditions:
            The user is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ )
            and user not logged into the account.
        Steps:
            The user filled in all fields except "Billing Last Name" and clicks the "Continue" button
        Expected results:
            Error message 'This is a required field.' appeared under the "Billing Last Name" field."""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_email(order_id=self.fake_order_id, email=self.email, billing_lastname='')
        page.continue_button().click()
        assert page.error_msg_billing_lastname_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле billing lastname не заполнено , а ошибка не показана"

    def test_email_field_not_filled(self, driver):
        """TC_012.009.004 | Footer > “Orders and Returns” > Email_field\n
        Pre-conditions:
            The user is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ )
             and user not logged into the account.
        Steps:
            The user filled in all fields except 'Email' and clicks the "Continue" button
        Expected results:
            Error message 'This is a required field.' appeared under the "Email" field."""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_email(order_id=self.fake_order_id, email='', billing_lastname=self.last_name)
        page.continue_button().click()
        assert page.error_msg_email_not_filled_or_incorrect_type().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле email не заполнено , а ошибка не показана"

    def test_zip_field_not_filled(self, driver):
        """TC_012.009.005 | Footer > “Orders and Returns” > ZIP code field\n
        Pre-conditions:
            The user is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ ) and user not logged into the account.
        Steps:
            1)The user selects "ZIP Code" in the "Find Order By" field\n
            2)The user filled in all fields except "Billing ZIP Code" and clicks the "Continue" button
        Expected results:
            Error message 'This is a required field.' appeared under the "Billing ZIP Code" field."""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_postcode(billing_lastname=self.last_name, order_id=self.fake_order_id, postcode='')
        page.continue_button().click()
        assert page.error_msg_billing_postcode_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле zipcode не заполнено , а ошибка не показана"

    # УТОЧНИТЬ БАГ ИЛИ НЕ БАГ
    # def test_ru_email(self, driver):
    #     page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
    #     page.open()
    #     page.fill_all_field_with_email(order_id=self.fake_order_id, email='почта@маил.рус',
    #                                    billing_lastname=self.last_name)
    #     page.continue_button().click()
    #     assert page.error_msg_email_not_filled_or_incorrect_type().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_EMAIL_TYPE, "Не появилась ошибка про неправильный формат email"


class TestCheckNonExistentOrder(FakeData):

    def test_by_email(self, driver):
        """TC_012.009.006 | Footer > “Orders and Returns” > Search for a non-existent order\n
        Pre-conditions:
            The user is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ )
             and user not logged into the account.
        Steps:
            The user fills in all fields with data for a non-existent order and clicks the "Continue" button
        Expected results:
            Error message -  'You entered incorrect data. Please try again.'
            appeared below the "Orders and Returns" heading."""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_email(billing_lastname=self.last_name, order_id=self.fake_order_id,
                                       email=self.email)
        page.continue_button().click()
        assert page.error_msg_incorrect_data().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_INCORRECT_DATA, "Поле zipcode не заполнено , а ошибка не показана"

    def test_by_postcode(self, driver):
        """TC_012.009.008 | Footer > “Orders and Returns” > Search for a non-existent order\n
        Pre-conditions:
            The user is on the page  (url = https://magento.softwaretestingboard.com/sales/guest/form/ )
             and user not logged into the account.
        Steps:
            1)The user selects "ZIP Code" in the "Find Order By" field\n
            2)The user fills in all fields with data for a non-existent order and clicks the "Continue" button\n
        Expected results:
            Error message -  'You entered incorrect data. Please try again.'
            appeared below the "Orders and Returns" heading."""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_postcode(billing_lastname=self.last_name, order_id=self.fake_order_id,
                                          postcode=self.postcode)
        page.continue_button().click()
        assert page.error_msg_incorrect_data().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_INCORRECT_DATA, "Поле zipcode не заполнено , а ошибка не показана"


class TestCheckExistingOrder(FakeData):

    # требуется регистрация , логин и плейсордер
    def test_by_email(self):
        """TC_012.009.007 | Footer > “Orders and Returns” > Search for an existing order By Email or ZIP Code\n
        Pre-conditions:
            The user is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ )
            and user not logged into the account.
        Steps:
            The user enters the correct data for the existing order in all required fields
            and clicks the “Continue” button.
        Expected results:
            There was a redirect to a page with information about the required order
            (url = https://magento.softwaretestingboard.com/sales/guest/view/ ) The header says "Order # 'NUMBER'",
             instead of the word 'NUMBER' the number of the order you are looking for should be displayed.
             The user sees all available information about the order, including status"""
        pass

    # требуется регистрация , логин и плейсордер
    def test_by_postcode(self):
        """TC_012.009.007 | Footer > “Orders and Returns” > Search for an existing order By Email or ZIP Code\n
            Pre-conditions:
                The user is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ )
                and user not logged into the account.
            Steps:
                1)The user selects "ZIP Code" in the "Find Order By" field
                2)The user enters the correct data for the existing order in all required fields
                and clicks the “Continue” button.
            Expected results:
                There was a redirect to a page with information about the required order
                (url = https://magento.softwaretestingboard.com/sales/guest/view/ ) The header says "Order # 'NUMBER'",
                instead of the word 'NUMBER' the number of the order you are looking for should be displayed.
                The user sees all available information about the order, including status"""
        pass


class TestChangeFindOrderBy:

    def test_switch_to_zip(self, driver):
        """TC_012.008.001 | Footer > “Orders and Returns” > Visibility and clickability > Verify the finding
         criterion is "Billing ZIP code" upon choosing "ZIP code" in "Find Order By" field/n
            Preconditions:
                A guest user is on the https://magento.softwaretestingboard.com/sales/guest/form/ page
            Steps:
                1)Find the order search criterion field name equal to "Email" by default
                2)Click on the "Find Order By" field
                3)Choose "ZIP code" option
            Expected result:
                Order finding criterion field name is 'Billing ZIP code'"""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL )
        page.open()
        page.select_find_order_by_postcode_dropdown()
        assert page.billing_postcode_field_name().text == OrdersAndReturnsPageLocators.TEXT_NAME_POSTCODE_FIELD, 'не произошло переключение поиска заказа с Email на ZIP'

    def test_switch_to_email(self, driver):
        """TC_012.008.002 | Footer > “Orders and Returns” > Visibility and clickability > Verify the finding
        criterion is "Email" upon choosing "Email" in "Find Order By" field/n
            Preconditions:
                A guest user is on the page https://magento.softwaretestingboard.com/sales/guest/form/
            Steps:
                1)Click on the "Find Order By" field
                2)Choose "ZIP code" option
                3)Make sure the "Find Order By" field is "ZIP code"
                4)Click on the "Find Order By" field
                5)Choose "Email" option
            Expected result:
                Order finding criterion field name is 'Email'"""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.select_find_order_by_postcode_dropdown()
        assert page.billing_postcode_field_name().text == OrdersAndReturnsPageLocators.TEXT_NAME_POSTCODE_FIELD, 'не произошло переключение поиска заказа с Email на ZIP'
        page.select_find_order_by_email_dropdown()
        assert page.email_field_name().text == OrdersAndReturnsPageLocators.TEXT_NAME_EMAIL_FIELD, 'не произошло переключение поиска заказа с ZIP на Email'
