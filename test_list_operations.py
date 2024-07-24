import pytest
from list_operations import reverse_list, find_max_min, remove_duplicates

def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a']
    assert reverse_list([]) == []

def test_find_max_min():
    assert find_max_min([1, 5, 3, 9, 2]) == (9, 1)
    assert find_max_min([-1, -5, 0, 10]) == (10, -5)
    with pytest.raises(ValueError):
        find_max_min([])

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates(['a', 'b', 'a', 'c', 'b']) == ['a', 'b', 'c']
    assert remove_duplicates([]) == []
