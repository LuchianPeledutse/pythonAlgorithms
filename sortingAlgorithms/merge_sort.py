import math
from typing import List




def merge(A: List, p: int, q: int, r:int) -> None:
    """
    Merges parts of array A from p to q and from q+1 to r
    Note: two parts are considered to be sorted themselves

    Args
    ----
    A: List 
        List to be sorted
    p: int
        Index value to sort from
    r: int
        Index value to sort to
    
    Note: p < r
    """
    N_l = q-p+1
    N_r = r-q
    L, R = [], []
    # Fill the left and right arrays
    for i in range(0, N_l):
        L.append(A[p + i])
    for j in range(0, N_r):
        R.append(A[q + j + 1])
    i = 0
    j = 0
    k = p
    # Compare items from left and right stacks to put them in correct order
    while i < N_l and j < N_r:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    # Fill the remaining part of A with items from the stack that is not empty
    # From left
    while i < N_l:
        A[k] = L[i]
        i += 1
        k += 1
    # From right
    while j < N_r:
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort(A: List, p: int, r: int) -> None:
    if p >= r:
        return 
    else:
        q = math.floor((p + r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

