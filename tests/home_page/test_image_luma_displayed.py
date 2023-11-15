from data.home_page_url import HOME_PAGE
from base.seleniumbase import  BasePage
from locators.base_page_locators import BasePageLocators


def test_image_luma_displayed(driver):
    page = BasePage(driver, url=HOME_PAGE)
    page.open()
    assert page.is_visible(BasePageLocators.LOGO_TITLE)

