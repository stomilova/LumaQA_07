class TestHoodiesSweatshirtsFilter:
    def test_product_are_visible(self, page_with_hs_filter):
        """
        TC_008.014.001 | Men > Tops > Hoodies & Sweatshirts filter
                        > Products are visible on the page
        """

        page = page_with_hs_filter

        assert page.is_products_displayed(), "Element is not displayed on the page"

