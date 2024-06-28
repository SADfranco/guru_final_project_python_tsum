import allure
from allure_commons.types import Severity
import jsonschema
from tsum_tests.helper.api_requests import api_call
from tsum_tests.helper.load_schema import load_schema


@allure.tag('api')
@allure.tag('regress')
@allure.title('Add item to cart')
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "SADfranco")
@allure.feature("Sell items")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_add_to_chart(add_headers):
    schema = load_schema('add_item_to_cart.json')

    endpoint = "/v6/cart/item"
    item = 13462198
    quantity = 1
    payload = {
        "type": "sku",
        "id": f"{item}",
        "quantity": quantity
    }

    response = api_call.api_post(endpoint, headers=add_headers, json=payload)

    body = response.json()
    assert response.status_code == 200
    jsonschema.validate(body, schema)
    assert body["items"][0]["item_id"] == item
    assert body["items"][0]["sku"]["id"] == item
