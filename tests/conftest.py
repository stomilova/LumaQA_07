from time import strftime, sleep

import pytest
from faker import Faker
from pages.account.create_account import CreateAccountPage
from pages.login.login_page import LoginPage
from locators.login import LOGIN_PAGE, LOGAUT_PAGE


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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def check_if_failed(request, driver):
    yield
    if request.node.rep_setup.passed and request.node.rep_call.failed:
        fn = f'{request.node.nodeid}_{strftime("%H_%M")}.png'.replace("/", "-").replace(":", "_")
        driver.save_screenshot(fn)


@pytest.fixture
def authorization(driver):
    page = LoginPage(driver, LOGIN_PAGE)
    page.open()
    page.sign_in()
    yield
    page = LoginPage(driver, LOGAUT_PAGE)
    page.open()
