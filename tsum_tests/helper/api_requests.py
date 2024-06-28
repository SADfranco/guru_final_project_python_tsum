import requests
import allure
from tsum_tests.utils import attach


class ApiCall:
    def send_request(self, method, url, **kwargs):
        with allure.step(f"Send API {method} Request to endpoint {method}"):
            response = requests.request(method=method, url=url, **kwargs)

            attach.request_url_and_body(response)
            attach.response_json_and_cookies(response)
            attach.logging_response(response)

            return response


api_call = ApiCall()
