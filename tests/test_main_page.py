from pages.main_page import MainPage


class TestMainPage:
    def test_verify_visability_the_title(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.check_visability_the_title()
