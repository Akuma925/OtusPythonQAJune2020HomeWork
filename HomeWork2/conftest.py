import pytest
from .Common.api_client import APIClient


# def pytest_addoption(parser):
#     parser.addoption("--url", default="https://dog.ceo/api")
#     parser.addoption("--status_code", default=200)


# @pytest.fixture(scope="session")
# def api_client(request):
#     base_url = request.config.getoption("--url")
#     status_code = request.config.getoption("--status_code")
#     return APIClient(base_address=base_url,status_code=status_code)
