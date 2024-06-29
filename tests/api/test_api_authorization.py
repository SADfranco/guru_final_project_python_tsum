import os
import allure
from allure_commons.types import Severity
import jsonschema
from tsum_tests.helper.api_requests import api_call
from tsum_tests.helper.load_schema import load_schema


@allure.tag('api')
@allure.label("layer", "API Tests")
@allure.tag('regress')
@allure.title('Authorization existing user')
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "SADfranco")
@allure.feature("Authorization")
@allure.link("https://www.tsum.ru/personal/profile/", name="Login Page")
def test_authorize_existing_user(base_endpoint, add_headers):
    schema = load_schema('successful_authorize.json')

    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")
    userid = os.getenv("TEST_USER_ID")
    payload = {
        "data": {
            "type": "authorize",
            "attributes": {
                "credential": email,
                "secret": password
            }
        }
    }

    response = api_call.send_request(method='POST', url=base_endpoint[1], headers=add_headers, json=payload)

    body = response.json()
    assert response.status_code == 200
    jsonschema.validate(body, schema)
    assert body["data"]["type"] == "authorizeResponse"
    assert body["data"]["attributes"]["email"] == email
    assert body["data"]["attributes"]["userId"] == userid
