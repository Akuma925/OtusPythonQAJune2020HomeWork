


# Тестируем получение List Breweries с использованием тегов by_city (используя параметризацию по городам), выдаем json
# Проверяем совпадение в полученном json значения по ключу город с городом из запроса в url
# При запросе несуществующего города получаем пустой list, а не ошибку.
def test_city(api_client,url_city):
    response = api_client.get(f'/breweries?by_city={url_city}')
    json_response = response.json()
    if len(json_response) != 0:
        for bar in json_response:
            assert bar.get('city') == url_city
    else:
        print("This response return empty json")


# Тестируем получение json by_type, с параметризацией из списка элементов (micro, regional, brewpub, large, planning,
# bar, contract, proprietor). Проверяем наличие в json в словарях ключа brewery_type со значением из url-запроса.
def test_type(api_client,fixture_by_type):
    response = api_client.get(f'/breweries?by_type={fixture_by_type}')
    json_response = response.json()
    for brewery_type in json_response:
        assert fixture_by_type == brewery_type.get('brewery_type')


def test_type_and_city(api_client,fixture_by_type, url_city):
    response = api_client.get(f'/breweries?by_type={fixture_by_type}&by_city={url_city}')
    json_response = response.json()
    assert type(json_response) == list


# Тестируем совпадение ID и названия бара, полученного через Get Brewery по данному ID
def test_id_get_brewery(api_client, test_input, expected_result):
    response = api_client.get(f'/breweries/{test_input}')
    json_response = response.json()
    assert json_response.get('name') == expected_result