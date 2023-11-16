import pytest
from data.home_page_url import HOME_PAGE
from base.seleniumbase import BasePage


@pytest.fixture()
def open_main_page(driver):
    base_page = BasePage(driver=driver, url=HOME_PAGE)
    base_page.open()
    return base_page
