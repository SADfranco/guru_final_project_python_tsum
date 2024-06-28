import allure
from allure_commons.types import Severity
import jsonschema
from tsum_tests.helper.api_requests import api_call
from tsum_tests.helper.load_schema import load_schema


@allure.tag('api')
@allure.tag('regress')
@allure.title('Check non existing email')
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SADfranco")
@allure.feature("Authorization")
@allure.link("https://www.tsum.ru/personal/profile/", name="Main Page")
def test_login_non_existing_user_by_email(base_endpoint, add_headers):
    schema = load_schema('non_existing_email.json')

    email = "andrew@yandex.ru"
    payload = {"data":
                   {"type": "checkEmail",
                    "attributes":
                        {"email": email}}}
    response = api_call.send_request(method='POST', url=f'{base_endpoint[1]}/check-email', headers=add_headers,
                                     json=payload)

    body = response.json()
    assert response.status_code == 404
    jsonschema.validate(body, schema)
    assert body['errors'][0]['title'] == 'Клиент не найден'
