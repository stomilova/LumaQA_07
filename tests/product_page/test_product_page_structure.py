import pytest
from data.product_page_data import PRODUCT_PAGE_URL_LIST, TIMEOUT
from locators.product_page_locators import ProductPageLocators
from pages.product_page.product_page import ProductPage

@pytest.mark.parametrize("url", PRODUCT_PAGE_URL_LIST)
def test_product_page_structure(driver, url):
    """
    TC_002.002.001
    """
    product_page = ProductPage(driver, url)
    product_page.open()
    assert product_page.is_visible(ProductPageLocators.HEADER, TIMEOUT)
    assert product_page.is_visible(ProductPageLocators.NAVIGATION_SECTION, TIMEOUT)
    assert product_page.is_visible(ProductPageLocators.BREADCRUMBS, TIMEOUT)
    assert product_page.is_visible(ProductPageLocators.BODY, TIMEOUT)
    assert product_page.is_visible(ProductPageLocators.FOOTER, TIMEOUT)
    assert product_page.is_visible(ProductPageLocators.COPYRIGHT, TIMEOUT)
