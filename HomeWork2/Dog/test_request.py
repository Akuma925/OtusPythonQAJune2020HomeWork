import pytest


def test_get_random(api_client):
    response = api_client.get("/api/breeds/image/random")
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.json()["status"] == "success"


def test_get_list_all_breed(api_client):
    response = api_client.get("/api/breeds/list/all")
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.json()["status"] == "success"


def test_get_by_breed(api_client):
    response = api_client.get("/api/breed/hound/images")
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.json()["status"] == "success"


def test_get_list_all_subbreed(api_client):
    response = api_client.get("/api/breed/hound/list")
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.json()["status"] == "success"


@pytest.mark.parametrize("breed", ["afghan", "basset", "plott", "walker"])
def test_get_list_breed(api_client, breed):
    response = api_client.get(f'/api/breed/hound/{breed}/images/random')
    assert response.status_code == 200
    assert response.reason == "OK"

