import pytest
from faker import Faker

from base.seleniumbase import BasePage
from locators.login import LOGIN_PAGE, LOGAUT_PAGE
from pages.account.create_account import CreateAccountPage
from pages.login.login_page import LoginPage


@pytest.fixture
def first_name():
    return Faker().first_name()


@pytest.fixture
def last_name():
    return Faker().last_name()


@pytest.fixture
def email():
    return Faker().email()


@pytest.fixture
def password():
    return Faker().password()


@pytest.fixture
def create_account(driver):
    CreateAccountPage(driver)


@pytest.fixture
def authorization(driver):
    page = LoginPage(driver, LOGIN_PAGE)
    page.open()
    page.sign_in()
    yield
    page = LoginPage(driver, LOGAUT_PAGE)
    page.open()


@pytest.fixture
def any_page_precondition(driver, any_url):
    base_page = BasePage(driver=driver, url=any_url)
    base_page.open()
    return base_page
