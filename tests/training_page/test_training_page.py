from pages.training_page.training_page import TrainingPage


class TestTrainingPage:
    def test_open_Training_page(self, driver):
        page = TrainingPage(driver, url=TrainingPage.URL)
        page.open()
        page.click_training_menu()
        expected_url = "https://magento.softwaretestingboard.com/training.html"
        assert driver.current_url == expected_url, 'Wrong URL'
