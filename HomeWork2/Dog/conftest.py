import pytest
from ..Common.api_client import APIClient


@pytest.fixture(scope="session")
def api_client(request):
    base_url = "https://dog.ceo"
    return APIClient(base_address=base_url, status_code=200)
