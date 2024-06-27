import allure
from utils import attach
import requests
from jsonschema import validate
from schemas.search_item import search_item


class Search:
    def search_kind_of_item(self, url, headers, kind):
        payload = {
            "q": kind
        }
        with allure.step('Send request on authorization'):
            response = requests.post(url=url, headers=headers, json=payload)
        attach.request_url_and_body(response)
        attach.response_json_and_cookies(response)
        attach.logging_response(response)

        return response

    def check_response(self, response):
        with allure.step("Check response and json schema"):
            body = response.json()
            items_model = [element["id"] for element in body]

            assert response.status_code == 200

            validate(body, search_item)

            assert len(items_model) == len(set(items_model))


searching_item = Search()
