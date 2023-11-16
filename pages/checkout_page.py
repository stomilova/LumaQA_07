from selenium.webdriver.common.by import By

from base.seleniumbase import BasePage
from locators.checkout_page_locators import CheckoutPageLocators


class CheckoutPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/checkout/"

    def email_field(self):
        return self.is_visible(CheckoutPageLocators.EMAIL_FIELD)

    def first_name_field(self):
        return self.is_visible(CheckoutPageLocators.FIRST_NAME_FIELD)

    def last_name_field(self):
        return self.is_visible(CheckoutPageLocators.LAST_NAME_FIELD)

    def street_address_1_field(self):
        return self.is_visible(CheckoutPageLocators.STREET_1_FIELD)

    def city_field(self):
        return self.is_visible(CheckoutPageLocators.CITY_FIELD)

    def postcode_field(self):
        return self.is_visible(CheckoutPageLocators.POSTCODE_FIELD)

    def country_dropdown_field(self):
        return self.is_visible(CheckoutPageLocators.COUNTRY_FIELD_DROPDOWN)

    def phone_number_field(self):
        return self.is_visible(CheckoutPageLocators.PHONE_NUMBER_FIELD)

    def select_state(self, state):
        self.is_visible(CheckoutPageLocators.STATE_FIELD_DROPDOWN)
        return self.is_clickable((By.XPATH, f"//*[@data-title='{state}']")).click()

    def select_flat_rate_shipping(self):
        return self.is_clickable(CheckoutPageLocators.SHIPPING_FLAT_RATE).click()

    def select_best_way_shipping(self):
        return self.is_clickable(CheckoutPageLocators.SHIPPING_BEST_WAY).click()

    def step_2_next_button(self):
        return self.is_clickable(CheckoutPageLocators.CHECKOUT_STEP_2_NEXT_BUTTON)

    def wait_overlay_closed(self):
        return self.is_invisible(CheckoutPageLocators.OVERLAY)

    def place_order_button(self):
        return self.is_clickable(CheckoutPageLocators.PLACE_ORDER_BUTTON)

    def place_order(self):
        self.place_order_button().click()
        self.wait_overlay_closed()

    def order_number_guest(self):
        return self.is_visible(CheckoutPageLocators.ORDER_NUMBER_GUEST)

    def fill_all_require_field_as_guest_us_shipping(self, state, email, firstname, lastname, street_1, city, postcode,
                                                    phone_number):
        self.select_state(state)
        self.email_field().send_keys(email)
        self.first_name_field().send_keys(firstname)
        self.last_name_field().send_keys(lastname)
        self.street_address_1_field().send_keys(street_1)
        self.city_field().send_keys(city)
        self.postcode_field().send_keys(postcode)
        self.phone_number_field().send_keys(phone_number)

    def full_guest_place_order_us_address_flat_shipping(self, state, email, firstname, lastname, street_1, city,
                                                        postcode,
                                                        phone_number) -> str:
        self.fill_all_require_field_as_guest_us_shipping(state, email, firstname, lastname, street_1, city, postcode,
                                                         phone_number)
        self.select_flat_rate_shipping()
        self.step_2_next_button().click()
        self.wait_overlay_closed()
        self.place_order()
        order_id = self.order_number_guest().text
        return order_id

    def full_guest_place_order_us_address_best_way_shipping(self, state, email, firstname, lastname, street_1, city,
                                                            postcode,
                                                            phone_number) -> str:
        self.fill_all_require_field_as_guest_us_shipping(state, email, firstname, lastname, street_1, city, postcode,
                                                         phone_number)
        self.select_best_way_shipping()
        self.step_2_next_button().click()
        self.wait_overlay_closed()
        self.place_order()
        order_id = self.order_number_guest().text
        return order_id
