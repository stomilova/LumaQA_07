from pages.item_page import ItemPageJackets


def test_related_products(driver):
    page = ItemPageJackets(driver, ItemPageJackets.URL)
    page.open()
    assert page.header_related() == 'Related Products', 'Не найдено названия сопутствующих товаров'
    assert page.related_item() > 0, 'Не найдены сопутствующие товары'





