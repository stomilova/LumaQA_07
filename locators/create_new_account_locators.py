from selenium.webdriver.common.by import By


class CreateNewAccountPageLocators:
    FIRST_NAME_FIELD = (By.XPATH, "//*[@id = 'firstname']")
    LAST_NAME_FIELD = (By.XPATH, "//*[@id = 'lastname']")
    EMAIL_FIELD = (By.XPATH, "//*[@id = 'email_address']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id = 'password']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//*[@id = 'password-confirmation']")

    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@title='Create an Account']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@id='send2' and @class='action login primary']")

    FIRST_NAME_LABEL = (By.CSS_SELECTOR, 'label[for="firstname"]')
    LAST_NAME_LABEL = (By.CSS_SELECTOR, 'label[for="lastname"]')
    EMAIL_LABEL = (By.CSS_SELECTOR, 'label[for="email_address"]')
    PASSWORD_LABEL = (By.CSS_SELECTOR, 'label[for="password"]')
    CONFIRM_PASSWORD_LABEL = (By.CSS_SELECTOR, 'label[for="password-confirmation"]')


    TEXT_THX_FOR_REGISTRATION_MSG = "Thank you for registering with Main Website Store."
    TEXT_USER_EXIST_REGISTRATION_MSG = "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account."


