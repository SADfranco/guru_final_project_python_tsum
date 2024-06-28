import allure
from allure_commons.types import Severity
import jsonschema
from tsum_tests.helper.api_requests import api_call
from tsum_tests.helper.load_schema import load_schema


@allure.tag('api')
@allure.tag('regress')
@allure.title('Get item page')
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SADfranco")
@allure.feature("Item info")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_get_item_page(base_endpoint, add_headers):
    schema = load_schema('item_info.json')

    model_id = "00083571"
    model_type = "-solntcezashchitnye-ochki-alexander-mcqueen-seryi"

    response = api_call.send_request(method='GET', url=f"{base_endpoint[2]}/item/{model_id}{model_type}",
                                     headers=add_headers)

    body = response.json()
    assert response.status_code == 200
    jsonschema.validate(body, schema)
    assert body['modelExtId'] == model_id
    assert body['slug'] == model_id + model_type
