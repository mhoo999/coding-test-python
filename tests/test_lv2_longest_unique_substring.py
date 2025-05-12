import pytest
from src.lv2_longest_unique_substring import solution

def test_examples():
    assert solution("abcabcbb") == 3  # "abc"
    assert solution("bbbbb") == 1     # "b"
    assert solution("pwwkew") == 3    # "wke"
    assert solution("") == 0
    assert solution("a") == 1
    assert solution("au") == 2
    assert solution("dvdf") == 3      # "vdf"
    assert solution("abba") == 2      # "ab" 또는 "ba"
    assert solution("tmmzuxt") == 5   # "mzuxt" 