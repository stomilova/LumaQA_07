import data.men_page_url as mp_url
from locators.men_page_locators import MenCategoryPageLocators as MCL


class TestHoodiesSweatshirtsFilter:
    def test_product_are_visible(self, page_with_hs_filter):
        """
        TC_008.014.001 | Men > Tops > Hoodies & Sweatshirts filter
                        > Products are visible on the page
        """

        page = page_with_hs_filter

        assert page.is_products_displayed(), "Element is not displayed on the page"

    def test_item_is_highlighted(self, page_with_hs_filter):
        """
        TC_008.014.002 | Men > Tops > Hoodies & Sweatshirts filter
                        > The item is highlighted with a shadow
        """

        page = page_with_hs_filter

        page.hover_first_item()

        assert page.is_shadow(), "The product is not highlighted with a shadow"

    def test_options_appear_on_the_products(self, page_with_hs_filter):
        """
        TC_008.014.003 | Men > Tops > Hoodies & Sweatshirts filter
                         > Options appear on the product item
        """

        page = page_with_hs_filter

        page.hover_first_item()

        assert page.is_options_displayed(), "Product options are not displayed"

