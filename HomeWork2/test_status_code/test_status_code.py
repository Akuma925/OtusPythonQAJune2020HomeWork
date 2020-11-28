def test_get_random(api_client):
    response = api_client.get(api_client.base_address)
    assert response.status_code == api_client.status_code



