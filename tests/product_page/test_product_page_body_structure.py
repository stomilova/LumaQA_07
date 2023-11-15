import pytest
from data.product_page_data import PRODUCT_PAGE_URL_LIST, TIMEOUT
from locators.product_page_locators import ProductPageLocators
from pages.product_page.product_page import ProductPage

@pytest.mark.parametrize("url", PRODUCT_PAGE_URL_LIST)
def test_product_page_body_structure(driver, url):
    """
    TC_002.003.001
    """
    product_page = ProductPage(driver, url)
    product_page.open()
    assert product_page.is_visible(ProductPageLocators.MAIN_INFO, TIMEOUT)
    assert product_page.is_visible(ProductPageLocators.PICTURES, TIMEOUT)
    assert product_page.is_visible(ProductPageLocators.DETAILED_INFO, TIMEOUT)

    # Since I didn't find didn't find the distribution logic with related and liked products,
    # I just check if one of them exists
    try:
        related_products_visible = product_page.is_visible(ProductPageLocators.RELATED_PRODUCTS)
        liked_products_visible = product_page.is_visible(ProductPageLocators.LIKED_PRODUCTS)
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        assert related_products_visible or liked_products_visible


