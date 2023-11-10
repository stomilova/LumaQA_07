import pytest
from selenium.webdriver.common.by import By
from pages.gear_page.category_page import BasePage

url_list = [
    'https://magento.softwaretestingboard.com/',
    'https://magento.softwaretestingboard.com/what-is-new.html',
    'https://magento.softwaretestingboard.com/women.html',
    'https://magento.softwaretestingboard.com/men.html',
    'https://magento.softwaretestingboard.com/gear.html',
    'https://magento.softwaretestingboard.com/training.html',
    'https://magento.softwaretestingboard.com/sale.html',
    'https://magento.softwaretestingboard.com/gear/bags.html',
    'https://magento.softwaretestingboard.com/gear/fitness-equipment.html',
    'https://magento.softwaretestingboard.com/gear/watches.html',
    'https://magento.softwaretestingboard.com/men/tops-men.html',
    'https://magento.softwaretestingboard.com/men/bottoms-men.html',
    'https://magento.softwaretestingboard.com/women/tops-women.html',
    'https://magento.softwaretestingboard.com/women/bottoms-women.html'
]

values_to_check = ['visibility', 'clickability'] 

expected_href = 'https://softwaretestingboard.com/write-for-us/'

WRITE_FOR_US_LINK = (By.XPATH,f"//footer//a[@href='{expected_href}']")

@pytest.mark.parametrize("param", values_to_check)
@pytest.mark.parametrize("any_url", url_list)
def test_check_visibility_or_clickability_of_the_title(param,any_url,driver):
    # can be used for every vis/click-ish check when we go to the page and check 
    """
    TC_012.001.001 | Footer > "Write for us" link > Visibility
        Steps:
            1. Open any page on The Site.
            2. Locate the Footer section.
            3. Verify the presence of the title "Write For Us" in the Footer.
        Expected results:
            The title "Write For Us" is visible in the footer of current page of The Site.

    TC_012.001.002 | Footer > "Write for us" link > Clickability
        Precondition:
            The User is on any page The Site and the title "Write For Us" is presence in the footer.
        Steps:
             Check the ability to click on the link
        Expected results:
            The link is clickable"""
    
    any_page = BasePage(driver=driver,url=any_url)
    any_page.open()

    if param == 'visibility':
        assert any_page.is_visible(locator=WRITE_FOR_US_LINK),f"Expected link '{expected_href}' isn't visible in the footer of page with '{any_url}'"
    else:
        assert any_page.is_clickable(locator=WRITE_FOR_US_LINK),f"Expected link '{expected_href}' isn't clickable in the footer of page with '{any_url}'"

