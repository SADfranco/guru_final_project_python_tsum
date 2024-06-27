import allure
from allure_commons.types import Severity
from tsum_tests.pages.mobile.main_screen import main_screen
from tsum_tests.pages.mobile.cart import add_to_cart
from tsum_tests.data.items import MobileItem


@allure.tag('Mobile')
@allure.tag('Android')
@allure.tag('regress')
@allure.title('Add item to cart')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Buy item")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_add_to_cart():
    test_item = MobileItem(
        kind='bag',
        name='Сумка The Tote Bag'
    )

    main_screen.skip_first_notifications()

    add_to_cart.search_item(test_item)

    add_to_cart.add_to_cart()

    add_to_cart.go_to_cart()

    add_to_cart.check_added_items(test_item)
