from base.seleniumbase import BasePage
from locators.base_page_locators import BasePageLocators
from locators.item_page_locators import ItemPageLocators


class ItemPage(BasePage):
    URL_DRIVEN_BACKPACK = "https://magento.softwaretestingboard.com/driven-backpack.html"

    def enter_quantity_items(self, quantity):
        self.is_clickable(ItemPageLocators.QUANTITY_OF_ITEM).clear()
        return self.is_clickable(ItemPageLocators.QUANTITY_OF_ITEM).send_keys(quantity)

    def add_driven_backpack_from_item_card_to_cart(self, quantity: int = 1):
        '''МОЖНО УКАЗАТЬ КОЛИЧЕСТВО И ДОБАВИТЬ СРАЗУ НЕСКОЛЬКО'''
        self.enter_quantity_items(quantity)
        self.is_clickable(ItemPageLocators.ADD_TO_CART_BUTTON).click()
        self.is_visible(BasePageLocators.MSG_SUCCESS)
