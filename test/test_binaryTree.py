import io
import sys
from contextlib import contextmanager
sys.path.append(r"C:\main\GitHub\pythonAlgorithms\dataStructures")

import pytest

import numpy as np

from binaryTree import BinaryNode, BinaryTree


ARRAY_SIZE = 1000
NUM_BINARY_TREES = 500


@contextmanager
def capture_stdout():
    """Context manager that captures stdout within the block"""
    old_stdout = sys.stdout
    captured = io.StringIO()
    sys.stdout = captured
    try:
        yield captured
    finally:
        sys.stdout = old_stdout

def tree_population(tree: BinaryTree, float_integer_keys: np.ndarray) -> BinaryTree:
    """
    Given array (shape (N, )) of integer keys in float format populates a given BinaryTree
    Population happens in list order (from first to last)
    """
    for one_key in float_integer_keys:
        tree.tree_insert(tree, BinaryNode(key=one_key.item(), data={}))
    return tree


# Create populated binary trees
binary_trees = [BinaryTree() for _ in range(NUM_BINARY_TREES)]
numpy_key_arrays = [np.random.randint(1, 1000, size=ARRAY_SIZE).astype(np.float16) for _ in range(NUM_BINARY_TREES)]
populated_tress = []
for tree, arr in zip(binary_trees, numpy_key_arrays):
    populated_tress.append(tree_population(tree, arr))

@pytest.mark.parametrize('tree', populated_tress)
def test_inorder_walk(tree: BinaryTree) -> None:
    """
    Tests whether the keys are printed in correct order after inorder walk
    """
    with capture_stdout() as captured:
        tree.inorder_walk()
    
    float_mapped_inorder = map(float, filter(None, [item.strip() for item in captured.getvalue().split('\n')]))
    current_float = float('-inf')
    for one_key in float_mapped_inorder:
        assert one_key >= current_float
        current_float = one_key