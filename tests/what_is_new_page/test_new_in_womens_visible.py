from pages.other_pages.what_is_new import NewPage
from locators.whats_new_page_locators import NewInWomenLocators

#006.001.001 User is able to see section NEW IN WOMEN’S (Divided into separate titles)

def test_headling_visible(driver):
    driver.get(NewPage.URL)
    find_headling = driver.find_element(*NewInWomenLocators.new_in_women_title)
    assert find_headling.text == NewInWomenLocators.new_in_women_title_text, f'Incorrect text: "{find_headling}"'


def test_hoodies_visible(driver):
    driver.get(NewPage.URL)
    find_hoodies = driver.find_element(*NewInWomenLocators.hoodies_title)
    assert find_hoodies.text == NewInWomenLocators.hoodies_text, f'Incorrect text: "{find_hoodies}"'


def test_jackets_visible(driver):
    driver.get(NewPage.URL)
    find_jackets = driver.find_element(*NewInWomenLocators.jackets_title)
    assert find_jackets.text == NewInWomenLocators.jackets_text, f'Incorrect text: "{find_jackets}"'


def test_tees_visible(driver):
    driver.get(NewPage.URL)
    find_tees = driver.find_element(*NewInWomenLocators.tees_title)
    assert find_tees.text == NewInWomenLocators.tees_text, f'Incorrect text: "{find_tees}"'


def test_bra_visible(driver):
    driver.get(NewPage.URL)
    find_bra = driver.find_element(*NewInWomenLocators.bra_title)
    assert find_bra.text == NewInWomenLocators.bra_text, f'Incorrect text: "{find_bra}"'


def test_pants_visible(driver):
    driver.get(NewPage.URL)
    find_pants = driver.find_element(*NewInWomenLocators.pants_title)
    assert find_pants.text == NewInWomenLocators.pants_text, f'Incorrect text: "{find_pants}"'


def test_shorts_visible(driver):
    driver.get(NewPage.URL)
    find_shorts = driver.find_element(*NewInWomenLocators.shorts_title)
    assert find_shorts.text == NewInWomenLocators.shorts_text, f'Incorrect text: "{find_shorts}"'
