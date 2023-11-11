from data.fake_data import FakeData
from locators.create_new_account_locators import CreateNewAccountPageLocators
from pages.login.create_new_account import CreateNewAccountPage
from pages.my_account.account_information_page import AccountInformationPage
from pages.my_account.address_book_page import AddressBookPage
from pages.my_account.my_account_page import MyAccountPage
from pages.my_account.my_downloadable_products_page import MyDownloadableProductsPage
from pages.my_account.my_orders_page import MyOrdersPage
from pages.my_account.my_product_reviews_page import MyProductReviewsPage
from pages.my_account.my_wish_list_page import MyWishListPage
from pages.my_account.stored_payment_methods_page import StoredPaymentMethodsPage


class TestMyAccountSwitchingButtons(FakeData):
    """TC_004.012.001 | Authorization > Visibility of stored
     information in User's account and redirection to the respective pages/n
     Pre-conditions:
         The user is logged in and is on the "My Account" page. ( url = https://magento.softwaretestingboard.com/customer/account )
         "My account" button selected.
     Steps:
         1)User clicks on the "My orders" button
         2)User clicks on the "My downloadable products" button
         3)User clicks on the "My Wish List" button
         4)User clicks on the "Address Book" button
         5)User clicks on the "Account information" button
         6)User clicks on the "Saved payment methods" button
         7)User clicks on the "My product reviews" button
         8)User clicks on the "My account" button
     Expected results:
         1)The "My Orders" page opens  (url = https://magento.softwaretestingboard.com/sales/order/history/ )
         2)The "My Downloadable Products" page opens (url = https://magento.softwaretestingboard.com/downloadable/customer/products/)
         3)The "My Wish List" page opens (url = https://magento.softwaretestingboard.com/wishlist/)
         4)If the user added an address earlier, "Address Book" page opens (url = https://magento.softwaretestingboard.com/customer/address/) otherwise “Add New Address“ page opens (url = https://magento.softwaretestingboard.com/customer/address/new/)
         5)The "Edit Account Information" page opens  (url = https://magento.softwaretestingboard.com/customer/account/edit/)
         6)The "Stored Payment Methods" page opens (url = https://magento.softwaretestingboard.com/vault/cards/listaction/ )
         7)The "My Product Reviews" page opens and (url = https://magento.softwaretestingboard.com/review/customer/)
         8)The "My Account" page opens (url = https://magento.softwaretestingboard.com/customer/account/)"""
    def test_my_orders_button(self, driver):
        page = CreateNewAccountPage(driver, CreateNewAccountPage.URL)
        page.open()
        page.create_new_account(self.first_name, self.last_name, self.email, self.password)
        assert page.success_create_account_msg().text == CreateNewAccountPageLocators.TEXT_THX_FOR_REGISTRATION_MSG, 'Не удалось зарегистрироваться'

        page = MyAccountPage(driver, page.driver.current_url)
        page.my_orders_button().click()
        assert page.driver.current_url == MyOrdersPage.URL, "Не удалось перейти на страницу 'My Orders'"

    def test_my_downloadable_products_button(self, driver):
        page = CreateNewAccountPage(driver, CreateNewAccountPage.URL)
        page.open()
        page.create_new_account(self.first_name, self.last_name, self.email, self.password)
        assert page.success_create_account_msg().text == CreateNewAccountPageLocators.TEXT_THX_FOR_REGISTRATION_MSG, 'Не удалось зарегистрироваться'

        page = MyAccountPage(driver, page.driver.current_url)
        page.my_downloadable_products_button().click()
        assert page.driver.current_url == MyDownloadableProductsPage.URL, "Не удалось перейти на страницу 'DOWNLOADABLE PRODUCTS'"

    def test_my_wish_list_button(self, driver):
        page = CreateNewAccountPage(driver, CreateNewAccountPage.URL)
        page.open()
        page.create_new_account(self.first_name, self.last_name, self.email, self.password)
        assert page.success_create_account_msg().text == CreateNewAccountPageLocators.TEXT_THX_FOR_REGISTRATION_MSG, 'Не удалось зарегистрироваться'

        page = MyAccountPage(driver, page.driver.current_url)
        page.my_wish_list_button().click()
        assert page.driver.current_url == MyWishListPage.URL, "Не удалось перейти на страницу 'WISH LIST'"

    def test_address_book_button(self, driver):
        page = CreateNewAccountPage(driver, CreateNewAccountPage.URL)
        page.open()
        page.create_new_account(self.first_name, self.last_name, self.email, self.password)
        assert page.success_create_account_msg().text == CreateNewAccountPageLocators.TEXT_THX_FOR_REGISTRATION_MSG, 'Не удалось зарегистрироваться'

        page = MyAccountPage(driver, page.driver.current_url)
        page.address_book_button().click()
        assert page.driver.current_url == AddressBookPage.URL_USER_HAS_NO_ADDRESS, "Не удалось перейти на страницу 'ADRESS BOOK'"

    def test_account_information_button(self, driver):
        page = CreateNewAccountPage(driver, CreateNewAccountPage.URL)
        page.open()
        page.create_new_account(self.first_name, self.last_name, self.email, self.password)
        assert page.success_create_account_msg().text == CreateNewAccountPageLocators.TEXT_THX_FOR_REGISTRATION_MSG, 'Не удалось зарегистрироваться'

        page = MyAccountPage(driver, page.driver.current_url)
        page.account_information_button().click()
        assert page.driver.current_url == AccountInformationPage.URL, "Не удалось перейти на страницу 'ACCOUNT INFORMATION'"

    def test_stored_payment_methods_button(self, driver):
        page = CreateNewAccountPage(driver, CreateNewAccountPage.URL)
        page.open()
        page.create_new_account(self.first_name, self.last_name, self.email, self.password)
        assert page.success_create_account_msg().text == CreateNewAccountPageLocators.TEXT_THX_FOR_REGISTRATION_MSG, 'Не удалось зарегистрироваться'

        page = MyAccountPage(driver, page.driver.current_url)
        page.stored_payment_methods_button().click()
        assert page.driver.current_url == StoredPaymentMethodsPage.URL, "Не удалось перейти на страницу 'PAYMENT METHODS'"

    def test_my_product_review_button(self, driver):
        page = CreateNewAccountPage(driver, CreateNewAccountPage.URL)
        page.open()
        page.create_new_account(self.first_name, self.last_name, self.email, self.password)
        assert page.success_create_account_msg().text == CreateNewAccountPageLocators.TEXT_THX_FOR_REGISTRATION_MSG, 'Не удалось зарегистрироваться'

        page = MyAccountPage(driver, page.driver.current_url)
        page.my_product_reviews_button().click()
        assert page.driver.current_url == MyProductReviewsPage.URL, "Не удалось перейти на страницу 'MY PRODUCT REVIEW'"

    def test_my_account_button(self, driver):
        page = CreateNewAccountPage(driver, CreateNewAccountPage.URL)
        page.open()
        page.create_new_account(self.first_name,self.last_name, self.email , self.password)
        assert page.success_create_account_msg().text == CreateNewAccountPageLocators.TEXT_THX_FOR_REGISTRATION_MSG , 'Не удалось зарегистрироваться'

        page = MyAccountPage(driver, page.driver.current_url)
        page.my_orders_button().click()
        assert page.driver.current_url == MyOrdersPage.URL, "Не удалось перейти на страницу 'MyOrders'"
        page.my_account_button().click()
        assert page.driver.current_url == MyAccountPage.URL, "Не удалось перейти на страницу 'My Account'"