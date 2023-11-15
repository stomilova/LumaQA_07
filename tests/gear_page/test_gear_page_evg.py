from data.gear_page_urls import GEAR_PAGE
from locators.gear_page_locators import BannerLocators
from base.seleniumbase import BasePage

def test_sprite_yoga_companion_kit_is_visible(driver):
    """TC_009.003.001 | Gear page > categories > Visibility of the 'Sprite Yoga Companion Kit' banner"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    assert page.is_visible(BannerLocators.SPRITE_YOGA_COMPANION_KIT_BANNER)