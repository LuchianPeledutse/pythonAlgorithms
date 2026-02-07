# Insertion sort algorithm
from typing import List
import random





def insertion_sort(the_list: List, list_length: int):
    if list_length == 1:
        return
    for ind in range(1, list_length):
        key = the_list[ind]
        j = ind - 1
        while j >= 0 and the_list[j] > key:
            the_list[j+1] = the_list[j]
            j -= 1
        # Insert the element in its proper place
        the_list[j+1] = key