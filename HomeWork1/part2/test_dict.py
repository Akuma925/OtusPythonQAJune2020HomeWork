import pytest


def test_copy(fixture_two):
    a = fixture_two
    a_copy = a.copy()
    assert a == a_copy


@pytest.mark.parametrize("test_data", ['1', '2', '3'])
def test_get(fixture_dict_keys, test_data):
    a = fixture_dict_keys
    res = a.get(test_data)
    assert res == a['1'] or res == a['2'] or res == a['3']


def test_clear(fixture_dict_keys):
    a = fixture_dict_keys
    a.clear()
    assert len(a) == 0


def test_values():
    a = {'1': 3, '2': 1}
    res = a.values()
    assert len(res) == 2


def test_item():
    a = {'1': 3, '2': 1}
    res = a.items()
    assert len(res) == 2
