import pytest
from pages.gear_page.category_page import BasePage
from locators.base_page_locators import BasePageLocators
from data.test_urls_list import TEST_URL_LIST


class TestFooterElementsVisibleClickable:
    PARAMETERS = [
        "visibility",
        "clickability",
    ]  # можно использовать данный список для отправки в  параметризацию, если нужно проверить два условия

    @pytest.mark.parametrize("param", PARAMETERS)
    @pytest.mark.parametrize("any_url", TEST_URL_LIST)
    def test_check_visibility_or_clickability_of_the_title_write_for_us(
        self, param, any_url, driver
    ):
        """
        TC_012.001.001 | Footer > "Write for us" link > Verify visibility of the link for the page for writing an article
            Steps:
                1. Open any page on The Site.
                2. Locate the Footer section.
                3. Verify the presence of the title "Write For Us" in the Footer.
            Expected results:
                The title "Write For Us" is visible in the footer of current page of The Site.

        TC_012.001.002 | Footer > "Write for us" link > Verify clickability of the link for the page for writing an article
            Precondition:
                The User is on any page The Site and the title "Write For Us" is presence in the footer.
            Steps:
                    Check the ability to click on the link
            Expected results:
                The link is clickable"""

        expected_link = "https://softwaretestingboard.com/write-for-us/"

        any_page = BasePage(driver=driver, url=any_url)
        any_page.open()
        any_page.verify_visability_or_clickability_of_the_element_in_location(
            param=param,
            element_value=f"The link to the '{expected_link}'",
            element_locator=BasePageLocators.WRITE_FOR_US_LINK,
            location="the footer",
        )

    @pytest.mark.parametrize("any_url", TEST_URL_LIST)
    def test_check_visibility_of_the_copyright(self, any_url, driver):
        """
        TC_012.011.001 | Footer > Self > Verify Copyright statement in the footer
            Steps:
                1. Open any page on the website.
                2. Locate the Footer section.
                3. Verify the presence of the copyright statement in the Footer.
            Expected results:
                The copyright information is visible in the footer of current page of the website.
        """

        any_page = BasePage(driver=driver, url=any_url)
        any_page.open()
        any_page.verify_visability_or_clickability_of_the_element_in_location(
            param="visibility",
            element_value="The copyright information",
            element_locator=BasePageLocators.COPYRIGHT_INFO,
            location="the footer",
        )

    @pytest.mark.parametrize("any_url", TEST_URL_LIST)
    def test_text_verification_of_the_copyright(self, any_url, driver):
        """
        TC_012.011.002 | Footer > Self > Text verification of Copyright information
            Precondition:
                User on any page of the website and the copyright information is visible in the Footer.
            Steps:
                Verify the text of the copyright information in the Footer.
            Expected results:
                The copyright information should have a text “Copyright © 2013-present Magento, Inc. All rights reserved.”
                opyright information is visible in the footer of current page of the website.
        """

        expected_text = "Copyright © 2013-present Magento, Inc. All rights reserved."
        any_page = BasePage(driver=driver, url=any_url)
        any_page.open()
        copyright_info = any_page.is_visible(locator=BasePageLocators.COPYRIGHT_INFO)
        assert (
            copyright_info.text == expected_text
        ), f"""
            The copiright information from this page {any_url} = '{copyright_info.text}' and mismatch to the expected text ('{expected_text}')"""
