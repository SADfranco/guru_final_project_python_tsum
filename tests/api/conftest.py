import pytest
from dotenv import load_dotenv

DOMAIN_URL = "https://api.tsum.ru"
CART_API = "/v6/cart"
AUTHORIZE_API = "/authorize"
CATALOG_API = "/v3/catalog"


@pytest.fixture()
def load_env():
    load_dotenv()


@pytest.fixture()
def base_endpoint():
    cart_endpoint = DOMAIN_URL + CART_API
    authorize_endpoint = DOMAIN_URL + AUTHORIZE_API
    catalog_endpoint = DOMAIN_URL + CATALOG_API
    return cart_endpoint, authorize_endpoint, catalog_endpoint


@pytest.fixture()
def add_headers():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36',
    }
    return headers
