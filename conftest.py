import pytest

from utils.client import ApiClient
from utils.user import UserClient


@pytest.fixture(scope="session")
def client():
    client = ApiClient("https://jsonplaceholder.typicode.com")
    return client


@pytest.fixture(scope="session")
def user_api_client():
    client = UserClient("https://jsonplaceholder.typicode.com")
    return client


@pytest.fixture(scope="session")
def username():
    return 'Delphine'
