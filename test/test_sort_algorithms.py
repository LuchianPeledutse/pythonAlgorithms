import sys
sys.path.append("../sortingAlgorithms")

import random
from typing import List

import pytest

from insertion_sort import insertion_sort
from merge_sort import merge_sort



def create_random_array(N:int, val_from:int = 100, val_to:int = 10_000) -> List:
    """Given a number of items N generates a random list with values from val_from to val_to"""
    return [random.randint(val_from, val_to) for _ in range(N)]

# Check insertion sort
check_lists = [(create_random_array(N), N) for N in range(1000)]
@pytest.mark.parametrize("the_list, list_length", check_lists)
def test_insertion_sort(the_list: List, list_length: int):
    test_list = the_list.copy()
    expected_list = the_list.copy()
    
    insertion_sort(test_list, list_length)
    expected_list.sort()
    
    assert test_list == expected_list, f"Failed for list of length {list_length}"

# Check merge sort
check_lists = [(create_random_array(N), N) for N in range(1000)]
@pytest.mark.parametrize("the_list, list_length", check_lists)
def test_merge_sort(the_list: List, list_length: int):
    test_list = the_list.copy()
    expected_list = the_list.copy()
    
    merge_sort(test_list, p = 0, r = len(test_list) - 1)
    expected_list.sort()
    
    assert test_list == expected_list, f"Failed for list of length {list_length}"