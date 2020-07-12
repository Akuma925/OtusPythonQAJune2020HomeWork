import pytest


def test_con():
    a = "Hello"
    b = " world!"
    assert "Hello world!" == a + b


def test_len(fixture_string):
    res = len(fixture_string)
    assert res == 5

def test_string_is_lower(fixture_str_lower):
    assert fixture_str_lower.islower()

def test_string_is_upper(fixture_string):
    assert fixture_string.isupper()

def test_string_capitalize(fixture_str_lower):
    assert fixture_str_lower.capitalize() == "Lower"
