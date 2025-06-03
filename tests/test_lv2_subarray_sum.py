import pytest
from src.lv2_subarray_sum import subarray_sum

def test_subarray_sum_basic():
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1, -1, 0], 0) == 3

def test_subarray_sum_edge():
    assert subarray_sum([], 0) == 0
    assert subarray_sum([0, 0, 0], 0) == 6
    assert subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4 