import pytest

from data import men_page_url as mp_url
from pages.men_category_page.category_page import MenCategoryPage


@pytest.fixture
def page_with_hs_filter(driver) -> MenCategoryPage:
    """
    Returns the open MenCategoryPage
    with the "Hoodies & Sweatshirts" filter on it.

    """

    page = MenCategoryPage(driver, url=mp_url.MEN_HOODIES_AND_SWEATSHIRTS_FILTER)
    page.open()

    return page

