from src.lv2_count_p_y import solution

def test_count_p_y_basic():
    assert solution("pPoooyY") is True
    assert solution("Pyy") is False
    assert solution("abc") is True
    assert solution("ppyY") is True
    assert solution("ppp") is False
    assert solution("yyy") is False

def test_count_p_y_edge():
    assert solution("p") is False
    assert solution("y") is False
    assert solution("") is True  # 빈 문자열도 True로 간주
    assert solution("PyPyPyPy") is True 