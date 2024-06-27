import allure
from utils import attach
import requests
from jsonschema import validate
from schemas.authorize import authorize


class Authorize:
    def authorize_existing_user(self, url, headers, email, password):
        payload = {
            "data": {
                "type": "authorize",
                "attributes": {
                    "credential": email,
                    "secret": password
                }
            }
        }
        with allure.step('Send request on authorization'):
            response = requests.post(url=url, headers=headers, json=payload)
        attach.request_url_and_body(response)
        attach.response_json_and_cookies(response)
        attach.logging_response(response)

        return response

    def check_response(self, email, userid, response):
        with allure.step("Check response and json schema"):
            body = response.json()
            assert response.status_code == 200

            validate(body, authorize)

            assert body["data"]["type"] == "authorizeResponse"
            assert body["data"]["attributes"]["email"] == email
            assert body["data"]["attributes"]["userId"] == userid


authorization = Authorize()
