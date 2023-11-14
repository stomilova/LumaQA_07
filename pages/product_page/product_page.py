from base.seleniumbase import BasePage

class ProductPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def page_title(self) -> str:
        return self.driver.title
