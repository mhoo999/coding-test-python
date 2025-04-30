import pytest
from src.lv1_sum_two_numbers import solution

def test_sum_two_numbers():
    assert solution(2, 3) == 5
    assert solution(-1, 1) == 0
    assert solution(0, 0) == 0
    assert solution(100, 200) == 300 