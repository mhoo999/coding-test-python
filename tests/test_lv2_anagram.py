import pytest
from src.lv2_anagram import solution

def test_anagram_true():
    assert solution("listen", "silent") is True
    assert solution("anagram", "nagaram") is True
    assert solution("aabbcc", "baccab") is True
    assert solution("123abc", "cba321") is True

def test_anagram_false():
    assert solution("hello", "bello") is False
    assert solution("rat", "car") is False
    assert solution("abc", "ab") is False
    assert solution("aabbcc", "aabbc") is False
    assert solution("abc1", "abc2") is False

def test_edge_cases():
    assert solution("a", "a") is True
    assert solution("a", "b") is False
    assert solution("", "") is True  # 두 빈 문자열도 애너그램으로 간주 