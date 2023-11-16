import pytest

from pages.item_page import ItemPage


class TestItemInfo:
    @pytest.mark.parametrize('item', [ItemPage.URL_DRIVEN_BACKPACK,
                                      ItemPage.URL_LUCIA_CROSS_FIT_BRA,
                                      ItemPage.URL_HARMONY_LUMAFLEX_STRENGTH_BAND_KIT])
    def test_item_rating_display(self, driver, item):
        """TC_002.009.001 | Product page > Main info > Rating block"""
        page = ItemPage(driver, url=item)
        page.open()
        review_counts = page.item_review_count()
        page.item_review().click()

        assert page.customer_review_header(), 'Не открылся блок с отзывами'
        assert page.get_overall_rating(review_counts) == page.item_rating(), 'Неправильное отображение рейтинга'

    def test_add_review_link(self, driver):
        """TC_002.009.002 | Product page > Main info > Add review link"""
        page = ItemPage(driver, url=ItemPage.URL_PUSH_IT_MESSENGER_BAG)
        page.open()
        page.add_your_review_link().click()

        assert page.block_review_add(), ' Не появился блок с добавлением нового отзыва'

    def test_item_name_and_sku(self, driver):
        """TC_002.008.001 | Product page > Main info > Name"""
        page = ItemPage(driver, url=ItemPage.URL_DRIVEN_BACKPACK)
        page.open()

        assert page.item_name(), 'Имя товара не отображается '
        assert page.item_sku_number(), 'SKU# товара не отображается'
