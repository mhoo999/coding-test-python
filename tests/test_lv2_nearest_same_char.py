from src.lv2_nearest_same_char import solution

def test_nearest_same_char_basic():
    assert solution("banana") == [-1, -1, -1, 2, 2, 2]
    assert solution("foobar") == [-1, -1, 1, -1, -1, -1]
    assert solution("abacabad") == [-1, -1, 2, -1, 2, 4, 2, -1]

def test_nearest_same_char_edge():
    assert solution("a") == [-1]
    assert solution("aa") == [-1, 1]
    assert solution("abcabc") == [-1, -1, -1, 3, 3, 3]
    assert solution("abcdedcba") == [-1, -1, -1, -1, -1, 2, 4, 6, 8] 