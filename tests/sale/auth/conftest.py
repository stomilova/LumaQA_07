import pytest
from selenium.webdriver.chrome.service import Service
from webdriver.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from LumaQA_07.locators.login_page_locators import (LoginPageLocators)
from LumaQA_07.pages.login.login_page import LoginPage
from LumaQA_07.pages.sale_page import SalePage
from LumaQA_07.pages.checkout_page import CheckoutPage
from LumaQA_07.pages.login.login_page import MyAccountPage
from LumaQA_07.pages.sale_page import TeesPage, TeesPageProdact
from LumaQA_07.data.sale_page import CHECKOUT_PAGE
import time


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    print('\nquit browser...')
    driver.quit()


@pytest.fixture()
def login_form(driver):
    page = LoginPage(driver, url=LoginPageLocators.URL)
    page.open()
    page.sign_in()
    assert page.header().text == 'My Account', 'Не удалось войти'


@pytest.fixture()
def choice_sale(driver, login_form):
    page = MyAccountPage(driver, url=MyAccountPage.URL)
    page.open()
    page.check_visibility_of_sale_section()
    page.check_clickability_of_sale_section()

    section_button = driver.find_element(By.CSS_SELECTOR, '#ui-id-8')
    section_button.click()

    text_name_page = driver.find_element(By.XPATH, '//span[@data-ui-id="page-title-wrapper"]')
    assert text_name_page


@pytest.fixture()
def choice_tees_on_sale(driver, login_form, choice_sale):
    page = SalePage(driver, url=SalePage.URL)
    page.open()
    page.check_visibility_of_Tees_on_sale()
    page.check_clickability_of_Tees_on_sale()

    widget_button = driver.find_element(By.XPATH, '//*[contains(text(), "Tees on sale")]')
    widget_button.click()

    text_name_page = driver.find_element(By.CSS_SELECTOR, 'h1[id="page-title-heading"]')
    assert text_name_page


@pytest.fixture()
def choice_prodact(driver, login_form, choice_sale, choice_tees_on_sale):
    page = TeesPage(driver, url=TeesPage.URL)
    page.open()
    page.check_visibility_PRODUCTS_LIST()
    page.check_clickability_PRODUCTS_LIST()

    widget_button = driver.find_element(By.XPATH,
                                        '//div[@class="product details product-item-details"] // a[contains(text(), "Tiffany Fitness Tee")] ')
    widget_button.click()
    time.sleep(5)

    card = driver.find_element(By.CSS_SELECTOR, 'span[data-ui-id="page-title-wrapper"]')
    assert card

    size = driver.find_element(By.CSS_SELECTOR, 'div[id="option-label-size-143-item-167"]')
    size.click()
    time.sleep(5)

    color = driver.find_element(By.CSS_SELECTOR, 'div[id="option-label-color-93-item-58"]')
    color.click()

    qty = driver.find_element(By.CSS_SELECTOR, 'input[id="qty"]' and 'input[value="1"]')
    assert qty

    add_to_card = driver.find_element(By.CSS_SELECTOR, 'button[id="product-addtocart-button"]')
    add_to_card.click()
    time.sleep(5)

    message = driver.find_element(By.XPATH, '//*[contains(text(), "You added Tiffany Fitness Tee to your ")]')
    assert message


@pytest.fixture()
def add_prodact(driver, login_form, choice_sale, choice_tees_on_sale, choice_prodact):
    page = TeesPageProdact(driver, url=TeesPageProdact.URL)
    page.open()
    page.check_visibility_basket()
    page.check_clickability_basket()

    basket = driver.find_element(By.CSS_SELECTOR, 'a[class="action showcart"]')
    basket.click()

    basket_cart = driver.find_element(By.XPATH, '//a[contains(text(), "Tiffany Fitness Tee")]')
    assert basket_cart

    proceed_to_checkout_button = driver.find_element(By.CSS_SELECTOR, 'div button[id="top-cart-btn-checkout"]')
    proceed_to_checkout_button.click()

    assert CHECKOUT_PAGE


@pytest.fixture()
def checkout_prodact(driver, login_form, choice_sale, choice_tees_on_sale, choice_prodact, add_prodact):
    page = CheckoutPage(driver, url=CheckoutPage.URL)
    page.open()
    page.checkout_step_shipping()
    page.shipping_methods()
    page.checkout_order_summary()

    shipping_page = driver.find_element(By.CSS_SELECTOR, '#shipping')
    assert shipping_page

    order_summary = driver.find_element(By.XPATH, '//strong[contains(text(), "Tiffany Fitness Tee")]')
    assert order_summary



