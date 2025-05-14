from src.lv2_two_sum import solution

def test_two_sum_basic():
    assert solution([2, 7, 11, 15], 9) == [0, 1]
    assert solution([3, 2, 4], 6) == [1, 2]
    assert solution([3, 3], 6) == [0, 1]

def test_two_sum_edge():
    assert solution([1, 2], 3) == [0, 1]
    assert solution([0, 4, 3, 0], 0) == [0, 3]
    assert solution([-1, -2, -3, -4, -5], -8) == [2, 4] 