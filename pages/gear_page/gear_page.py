from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage
from data.gear_page_urls import GEAR_PAGE


class GearPage(BasePage):
    # page with categories

    def __init__(self, driver):
        super().__init__(url=GEAR_PAGE,driver=driver)


   
