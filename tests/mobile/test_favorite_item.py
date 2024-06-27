import allure
from allure_commons.types import Severity
from tsum_tests.pages.mobile.favorite_item import favorite_item
from tsum_tests.pages.mobile.main_screen import main_screen
from tsum_tests.data.items import MobileItem


@allure.tag('Mobile')
@allure.tag('Android')
@allure.tag('regress')
@allure.title('Check favorite item')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Add item to favorite")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_add_to_favorite():
    test_item = MobileItem(
        kind='bag',
        name='Сумка The Tote Bag'
    )

    main_screen.skip_first_notifications()

    favorite_item.search_item(test_item)

    favorite_item.add_to_favorite_list()

    favorite_item.go_to_favorite_tab()

    favorite_item.check_added_items_in_list(test_item)
