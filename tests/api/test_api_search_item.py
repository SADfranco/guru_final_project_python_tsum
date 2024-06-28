import allure
from allure_commons.types import Severity
import jsonschema
from tsum_tests.helper.api_requests import api_call
from tsum_tests.helper.load_schema import load_schema


@allure.tag('api')
@allure.tag('regress')
@allure.title('Searching item from main page')
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SADfranco")
@allure.feature("Search item")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_search_item(base_endpoint, add_headers):
    schema = load_schema('search_item.json')


    item = "Джинсы"
    payload = {
        "q": item
    }
    response = api_call.send_request(method='POST', url=f'{base_endpoint[2]}/search', headers=add_headers,
                                                                                               json=payload)

    body = response.json()
    items_model = [element["id"] for element in body]
    assert response.status_code == 200
    jsonschema.validate(body, schema)
    assert len(items_model) == len(set(items_model))
