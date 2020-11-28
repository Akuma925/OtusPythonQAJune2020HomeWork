import cerberus
import pytest


def test_api_json_schema_list_all_subbreeds(api_client):
    res = api_client.get(path="/api/breed/hound/list")

    schema = {
        "message": {"type": "list"},
        "status": {"type": "string"}
    }
    v = cerberus.Validator()
    assert v.validate(res.json(), schema)


def test_api_json_schema_list_all_breeds(api_client):
    res = api_client.get(path="/api/breeds/list/all")

    schema = {
        "message": {"type": "dict"},
        "status": {"type": "string"}
    }
    v = cerberus.Validator()
    assert v.validate(res.json(), schema)


def test_api_json_schema_by_breed(api_client):
    res = api_client.get(path="/api/breed/hound/images")

    schema = {
        "message": {"type": "list"},
        "status": {"type": "string"}
    }
    v = cerberus.Validator()
    assert v.validate(res.json(), schema)


@pytest.mark.parametrize("breed", ["afghan", "basset", "plott", "walker"])
def test_get_list_breed(api_client, breed):
    res = api_client.get(f'/api/breed/hound/{breed}/images/random')
    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }
    v = cerberus.Validator()
    assert v.validate(res.json(), schema)
