import allure
from allure_commons.types import Severity
import jsonschema
from tsum_tests.helper.api_requests import api_get
from tsum_tests.helper.load_schema import load_schema


@allure.tag('api')
@allure.tag('regress')
@allure.title('Get item page')
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SADfranco")
@allure.feature("Item info")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_get_item_page(add_headers):
    schema = load_schema('item_info.json')

    model_id = '00083571'
    model_type = '-solntcezashchitnye-ochki-alexander-mcqueen-seryi'
    endpoint = f"/v3/catalog/item/{model_id}{model_type}"

    response = api_get(endpoint, headers=add_headers)

    body = response.json()
    assert response.status_code == 200
    jsonschema.validate(body, schema)
    assert body['modelExtId'] == model_id
    assert body['slug'] == model_id + model_type
