import allure
from allure_commons.types import Severity
from tsum_tests.pages.api.add_to_cart import cart


@allure.tag('api')
@allure.tag('regress')
@allure.title('Add item to cart')
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "SADfranco")
@allure.feature("Sell items")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_add_to_chart(add_headers):
    url = "https://api.tsum.ru/v6/cart/item"
    item = 13462198
    quantity = 1

    response = cart.add_item_to_cart(url,add_headers, item, quantity)

    cart.check_response(item, response)
