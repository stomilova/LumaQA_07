from data.fake_data import FakeData


# from locators.orders_and_returns_locators import OrdersAndReturnsPageLocators
# from pages.checkout_page import CheckoutPage
# from pages.footer.orders_and_returns import OrdersAndReturnsPage
# from pages.item_page import ItemPage
# from pages.main_page import MainPage


class TestOrderAndPayments(FakeData):

    def test_order_and_payments_positive(self, open_main_page):
        print(open_main_page)
