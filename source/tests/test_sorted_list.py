"""SortedList class test module."""

from random import randint

from utils import SortedList


def test_sorted_list_is_always_sorted():
    """Tests that the sorted list structure is always sorted."""
    random_list = [randint(1, 100) for _ in range(100)]
    sorted_random_list = sorted(random_list)

    my_sorted_list = SortedList()
    for number in random_list:
        my_sorted_list.append(number)

    assert my_sorted_list == sorted_random_list
