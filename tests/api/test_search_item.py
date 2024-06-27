import allure
from allure_commons.types import Severity
from tsum_tests.pages.api.search_item import searching_item


@allure.tag('api')
@allure.tag('regress')
@allure.title('Searching item from main page')
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SADfranco")
@allure.feature("Searching item")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_authorize_existing_user(add_headers):
    url = "https://api.tsum.ru/v3/catalog/search"
    item = "Джинсы"

    response = searching_item.search_kind_of_item(url, add_headers, item)

    searching_item.check_response(response)
