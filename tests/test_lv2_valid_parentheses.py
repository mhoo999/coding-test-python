from src.lv2_valid_parentheses import solution

def test_valid_parentheses_true():
    assert solution("") is True
    assert solution("()") is True
    assert solution("()[]{}") is True
    assert solution("{[]}") is True
    assert solution("([]{})") is True
    assert solution("((({[]})))") is True

def test_valid_parentheses_false():
    assert solution("(") is False
    assert solution("(") is False
    assert solution("([)]") is False
    assert solution("(]") is False
    assert solution("({[})") is False
    assert solution("(()") is False
    assert solution(")(") is False 