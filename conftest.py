import pytest

from utils.client import ApiClient


@pytest.fixture(scope="session")
def client():
    client = ApiClient("https://jsonplaceholder.typicode.com")
    return client


@pytest.fixture(scope="session")
def username():
    return 'Delphine'
