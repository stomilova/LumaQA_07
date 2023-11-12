import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pages.gear_page.category_page import CategoryPage
from pages.gear_page.gear_page import GearPage
from data.gear_page_urls import BAGS_PAGE, FITNESS_EQ_PAGE, WATCHES_PAGE
from locators.gear_page_locators import GearPageLocators, CategoryPageLocators

total_categories = ["Bags", "Fitness Equipment", "Watches"]
category_list = ["Bags", "Fitness Equipment", "Watches"]
founded_categories = []

list_of_category_url = [
    BAGS_PAGE,
    FITNESS_EQ_PAGE,
    WATCHES_PAGE,
]


class TestGearPageCategory:
    """TC_009.001.001 - TC_009.002.006 for now"""

    def find_categories_and_counters_at_the_sidebar():
        """collect test data"""
        test_data = []
        options = Options()
        options.add_argument("--window-size=2880,1800")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        gear_page = GearPage(driver=driver)
        gear_page.open()
        sidebar = gear_page.is_visible(locator=GearPageLocators.SIDEBAR_MAIN)

        # Находим все элементы внутри контейнера
        categories = sidebar.find_elements(
            *GearPageLocators.SIDEBAR_ELEMENTS
        )  # * выбирает все дочерние элементы и мы уже проверили что эти элементы в сайдбаре

        # Теперь у вас есть список элементов внутри сайдбара
        assert len(categories) == len(
            category_list
        ), f"The number of categories is {len(categories)},(expected = {len(category_list)}).Check, it can be update in category list"

        for category in categories:
            category_xpath = (By.XPATH, f'//dd//a[text()="{category.text}"]')
            counter_xpath = (
                By.XPATH,
                f'{category_xpath[1]}/following-sibling::span[@class="count"]',
            )

            test_data.append([category_xpath, counter_xpath])
        driver.quit()
        return test_data

    def test_find_and_verify_title_of_sidebar(self, gear_page_precondition):
        """TC_009.001.001 | Gear page > categories > Shop By Category
        Pre-conditions:
            A user is on The Gear page
        Steps:
            Find and verify the title of the sidebar with the text 'Shop By Category'.
        Expected results:
        The title 'Shop By Category' is displayed on the sidebar."""

        gear_page = gear_page_precondition

        sidebar = gear_page.is_visible(locator=GearPageLocators.SIDEBAR_MAIN)

        # проверяем что, элементы находятся в сайдбаре
        title_1 = sidebar.find_element(*GearPageLocators.SHOP_BY_TITLE).text
        title_2 = sidebar.find_element(*GearPageLocators.CATEGORY_TITLE).text

        assert (
            f"{title_1} {title_2}" == "Shop By Category"
        ), f"""
            The title of the Sidebar - '{title_1} {title_2}'.
            Expected - 'Shop By Category'"""

    @pytest.mark.parametrize(
        "category_xpath,counter_xpath", find_categories_and_counters_at_the_sidebar()
    )
    def test_find_and_verify_category_at_the_sidebar(
        self, category_xpath, counter_xpath, gear_page_precondition
    ):
        """TC_009.001.(002-004) | Gear page > categories > category
        Pre-conditions:
            A user is on The Gear page and the sidebar with the text 'Shop By Category' is visible
        Steps:
            Find and verify the presence of the category .
        Expected results:
            The category is visible on the sidebar."""

        gear_page = gear_page_precondition

        category = gear_page.is_visible(locator=category_xpath)

        category_name = category.text
        assert (
            category_name in category_list
        ), f"We found another one category title - '{category_name}', Please check the locators at the Sidebar and list of categories"

        category_list.remove(
            category_name
        )  # удаляем из временного списка, чтоб проверить - нашлили мы все наши категории заданные по стори. лист может обновляться
        founded_categories.append(
            category_name
        )  # добавляем в новый лист, то что нашли, чтоб были видны сразу в резалте.

    def test_category_list(self):
        """Additional step to verify the total list of categories after the previous test cases"""

        missed_category = [
            cat for cat in total_categories if cat not in founded_categories
        ]  # if we miss something
        assert (
            not category_list
        ), f"Please check compare the we have found : {founded_categories}, we should found : {total_categories}. we miss {missed_category}"

    @pytest.mark.parametrize(
        "category_xpath,counter_xpath", find_categories_and_counters_at_the_sidebar()
    )
    def test_find_and_verify_location_of_counter_at_the_sidebar(
        self, gear_page_precondition, category_xpath, counter_xpath
    ):
        """TC_009.002.(001-003) | Gear page > categories > The counter for the category
        Pre-conditions:
            User is on The Gear Page and categories are displayed at the 'Shop By Category' sidebar.
        Steps:
            1)Locate the 'Shop By Category' sidebar.
            2)Verify that the current category is displayed.
            3)Find and verify the counter indicating the quantity of available products in the 'Bags' category.
        Expected results:
            The quantity counter for products with the category is located near the title at the sidebar and visible.
        """
        gear_page = gear_page_precondition
        category = gear_page.is_visible(locator=category_xpath)
        # проверяем что каунтер есть рядом с нашей категорией
        category_counter = gear_page.is_visible(locator=counter_xpath)

        assert (
            category_counter.text
        ), f"We found a counter for {category.text}, but it is empty"

    @pytest.mark.parametrize(
        "category_xpath,counter_xpath", find_categories_and_counters_at_the_sidebar()
    )
    def test_verify_category_counter_on_gear_and_category_page(
        self, driver, wait, gear_page_precondition, category_xpath, counter_xpath
    ):
        """TC_009.002.(004-006) | Gear page > categories >
        Verify the counter on the Gear Page for the category 'Bags' with counter on the Category Page
        Pre-conditions:
            User is on The Gear Page and category 'Bags' is located and visible.
        Steps:
            1. Find and verify the counter indicating the quantity of available products in the 'Bags' category.
            2. Click on the 'Bags' category to access the category page.
            3. Find the counter on the 'Bags' category page and note the quantity of available products.
            4. Compare the counter on the Gear page with the counter on the 'Bags' category page.
        Expected results:
            The counter on the Gear page match the counter on the respective category page.
        """
        gear_page = gear_page_precondition

        category = gear_page.is_visible(locator=category_xpath)
        category_name = category.text

        category_counter = gear_page.is_visible(locator=counter_xpath).text
        category_url = category.get_attribute("href")

        category_page = CategoryPage(driver=driver, url=category_url)

        category.click()
        wait.until(EC.url_to_be(category_url))

        # блок проверки редеректа - название страници категории состоит из двух значений "title - Gear"
        assert (
            driver.current_url == category_url
        ), f"We reached wrong url - {driver.current_url}, but expected - {category_url}"
        assert (
            driver.title.split(" - ")[0] == category_name
        ), f"We reach {driver.title}, but Expected to be at {category_name} page"

        counter_on_the_category_page = category_page.is_visible(
            locator=CategoryPageLocators.LAST_ITEM_COUNTER
        ).text

        assert int(category_counter) == int(
            counter_on_the_category_page
        ), f"""
        The counter of items for the category -{category_name} on the Gear Page {category_counter} 
        not equal to the counter on the category page {counter_on_the_category_page}"""
