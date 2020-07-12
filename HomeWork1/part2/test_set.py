import pytest


def test_assert():
    set_1 = set()
    set_2 = set()
    assert set_1 == set_2


@pytest.mark.parametrize("test_data", [5, 5, 5])
def test_add(fixture_two, test_data):
    a = set(fixture_two)
    a.add(test_data)
    assert len(a) == len(a)


def test_clear(fixture_two):
    a = set(fixture_two)
    a.clear()
    assert len(a) == 0


@pytest.mark.parametrize("test_data", [[11, 12, 13]])
def test_isdisjoint(test_data):
    a = [115, 152, 132, 113, 134]
    a1 = set(a)
    ch = set(test_data)
    assert a1.isdisjoint(ch)


def test_copy(fixture_two):
    a = set(fixture_two)
    a_copy = a.copy()
    assert a == a_copy
