import os
import allure
from allure_commons.types import Severity
from tsum_tests.pages.api.authorize import authorization




@allure.tag('api')
@allure.tag('regress')
@allure.title('Authorise existing user')
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "SADfranco")
@allure.feature("Authorization")
@allure.link("https://www.tsum.ru/personal/profile/", name="Login Page")
def test_authorize_existing_user(add_headers):
    url = "https://api.tsum.ru/authorize"
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")
    userid = os.getenv("TEST_USER_ID")

    response = authorization.authorize_existing_user(url, add_headers, email, password)

    authorization.check_response(email, userid, response)
