import pytest
from ..Common.api_client import APIClient
import json
import requests

@pytest.fixture(params=['dog', 'green', 'fun', 'bar', 'music', 'pub', 'dance'])
def fixture_query_name(request):
    return request.param


@pytest.fixture(params=['micro', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor'])
def fixture_by_type(request):
    return request.param


@pytest.fixture(scope="session")
def api_client(request):
    base_url = "https://api.openbrewerydb.org"
    status_code = 200
    return APIClient(base_address=base_url, status_code=status_code)


with open('url_city.json', "r") as json_file:
    tmp_data = json.load(json_file)
city_list = tmp_data["city"]


@pytest.fixture(name='url_city', params=city_list)
def get_url_city(request):
    yield request.param


def pytest_generate_tests( metafunc):
    if 'test_input' not in metafunc.fixturenames:
        return
    response = requests.get('https://api.openbrewerydb.org/breweries')
    if response.status_code == 200:
        json_response = response.json()
        brewery_list_all = []
        for brewery in json_response:
            brewery_id = brewery.get('id')
            brewery_name = brewery.get('name')
            brewery_list = [brewery_id, brewery_name]
            brewery_list_all.append(brewery_list)
        return metafunc.parametrize('test_input, expected_result', brewery_list_all)
    else:
        raise Exception('RequestException, HTTP Code != 200')
