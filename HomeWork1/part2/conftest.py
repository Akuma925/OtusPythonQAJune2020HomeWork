import pytest


@pytest.fixture(params=[[11, 12, 12, 13, 14],
                        [11, 12, 12, 13, 14, 15],
                        [11, 18, 12]])
def fixture_one(request):
    return request.param


@pytest.fixture(params=[[11, 12, 12, 13, 14]])
def fixture_two(request):
    return request.param

@pytest.fixture(params=[{'1':'11', '2':'12', '3':'13'}])
def fixture_dict_keys(request):
    return request.param

@pytest.fixture(params=['HELLO'])
def fixture_string(request):
    return request.param

@pytest.fixture(params=['lower'])
def fixture_str_lower(request):
    return request.param

