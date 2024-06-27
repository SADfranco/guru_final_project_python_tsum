import allure
from utils import attach
import requests
from jsonschema import validate
from schemas.item_to_cart import add_to_cart


class Cart:

    def add_item_to_cart(self, url, headers, item, quantity):
        payload = {
            "type": "sku",
            "id": f"{item}",
            "quantity": quantity
        }

        with allure.step('Send items to cart'):
            response = requests.post(url=url, headers=headers, json=payload)
        attach.request_url_and_body(response)
        attach.response_json_and_cookies(response)
        attach.logging_response(response)

        return response

    def check_response(self, item, response):
        with allure.step("Check response and json schema"):
            body = response.json()

            assert response.status_code == 200

            validate(body, add_to_cart)

            assert body["items"][0]["item_id"] == item
            assert body["items"][0]["sku"]["id"] == item


cart = Cart()
