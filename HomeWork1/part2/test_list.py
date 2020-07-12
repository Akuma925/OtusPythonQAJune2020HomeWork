import pytest

def test_assert():
    list1 = []
    list2 = []
    assert list1==list2

@pytest.mark.parametrize("test_data",[5,6,3])
def test_append(fixture_one,test_data):
    a = fixture_one
    assert len(a) == test_data

@pytest.mark.parametrize("test_data",[1,2,3,-3,4,5,5,'a'])
def test_clear(test_data):
    a = [test_data]
    a.clear()
    assert len(a) == 0
@pytest.mark.parametrize("test_data",[1,2,3,4,5,5,'a'])
def test_count(test_data):
    a = [1,2,3,4,4,4,5,6,6,8,88,88,9,6,6,6,2,'a']
    res = a.count(test_data)
    assert res == 1 or res == 2 or res == 3 or res == 5

@pytest.mark.parametrize("test_data",[1,2,3,-3,4,5,5,'a'])
def test_clear(test_data):
    a = [test_data]
    a.clear()
    assert len(a) == 0

@pytest.mark.parametrize("test_data",[1,2,3,-3,4,5,5,'a'])
def test_copy(fixture_two,test_data):
    a_copy = fixture_two.copy()
    assert fixture_two == a_copy
