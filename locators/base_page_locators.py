from selenium.webdriver.common.by import By


class BasePageLocators:
    HEADER = (By.CSS_SELECTOR, 'h1 span')
    MSG_ERROR = (By.CSS_SELECTOR, '[action nav-toggle')
    MSG_SUCCESS = (By.CSS_SELECTOR, '[data-ui-id="message-success"]')
    LOGO_TITLE = (By.CSS_SELECTOR, '[class="logo"]')
