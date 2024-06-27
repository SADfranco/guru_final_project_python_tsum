import allure
from allure_commons.types import Severity
import jsonschema
from tsum_tests.helper.api_requests import api_post
from tsum_tests.helper.load_schema import load_schema


@allure.tag('api')
@allure.tag('regress')
@allure.title('Check non existing email')
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SADfranco")
@allure.feature("Authorization")
@allure.link("https://www.tsum.ru/personal/profile/", name="Main Page")
def test_login_non_existing_user_by_email(add_headers):
    schema = load_schema('non_existing_email.json')

    endpoint = "/authorize/check-email"
    email = "andrew@yandex.ru"
    payload = {"data":
                   {"type": "checkEmail",
                    "attributes":
                        {"email": email}}}
    response = api_post(endpoint, headers=add_headers, json=payload)

    body = response.json()
    assert response.status_code == 404
    jsonschema.validate(body, schema)
    assert body['errors'][0]['title'] == 'Клиент не найден'
