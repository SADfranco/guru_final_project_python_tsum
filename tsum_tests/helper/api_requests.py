import requests
import allure
from tsum_tests.utils import attach

class ApiCall:
    def api_get(method, endpoint, **kwargs):
        with allure.step(f"Send API {method} Request to endpoint {endpoint}"):
            response = requests(method=method.upper(), url="https://api.tsum.ru" + endpoint, **kwargs)

            attach.request_url_and_body(response)
            attach.response_json_and_cookies(response)
            attach.logging_response(response)

            return response
            
api_call = ApiCall()
