from src.lv2_string_validation import solution

def test_string_validation_basic():
    assert solution("a234") is False
    assert solution("1234") is True
    assert solution("123456") is True
    assert solution("12345") is False
    assert solution("abcd") is False
    assert solution("0000") is True
    assert solution("12a4") is False

def test_string_validation_edge():
    assert solution("") is False
    assert solution("1") is False
    assert solution("1234567") is False
    assert solution("000000") is True 