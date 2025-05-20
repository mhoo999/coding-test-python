from src.lv2_sort_string_desc import solution

def test_sort_string_desc_basic():
    assert solution("Zbcdefg") == "gfedcbZ"
    assert solution("aAbBcC") == "cbaCBA"
    assert solution("HelloWorld") == "roollledWH"

def test_sort_string_desc_edge():
    assert solution("A") == "A"
    assert solution("z") == "z"
    assert solution("aA") == "aA"
    assert solution("abcABC") == "cbaCBA" 