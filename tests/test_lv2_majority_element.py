from src.lv2_majority_element import solution

def test_majority_element_basic():
    assert solution([3,2,3]) == 3
    assert solution([2,2,1,1,1,2,2]) == 2
    assert solution([1]) == 1
    assert solution([4,4,4,2,4,3,4,4]) == 4

def test_majority_element_edge():
    assert solution([5,5,5,5,5,5,5]) == 5
    assert solution([6,7,6,6,7,6,6]) == 6
    assert solution([9,8,9,9,8,8,9,9,8,9]) == 9 