import pytest
from pages.gear_page.gear_page import GearPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def gear_page_precondition(driver):
    gear_page = GearPage(driver=driver)
    gear_page.open()
    return gear_page


def driver_initiation_for_test_data():
    options = Options()
    options.add_argument("--window-size=2880,1800")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver
