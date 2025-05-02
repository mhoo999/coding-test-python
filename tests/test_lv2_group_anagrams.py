import pytest
from src.lv2_group_anagrams import solution

def test_group_anagrams():
    # 기본 테스트 케이스
    result = solution(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert len(result) == 3  # 3개의 그룹이 있어야 함
    
    # 각 그룹을 정렬하여 비교
    sorted_result = [sorted(group) for group in result]
    assert ["ate", "eat", "tea"] in sorted_result
    assert ["nat", "tan"] in sorted_result
    assert ["bat"] in sorted_result

def test_empty_string():
    # 빈 문자열 테스트
    assert solution([""]) == [[""]]

def test_single_char():
    # 단일 문자 테스트
    assert solution(["a"]) == [["a"]]

def test_no_anagrams():
    # 애너그램이 없는 경우
    result = solution(["cat", "dog", "pig"])
    assert len(result) == 3
    assert all(len(group) == 1 for group in result)

def test_all_same_anagrams():
    # 모두 같은 애너그램인 경우
    result = solution(["abc", "bca", "cab"])
    assert len(result) == 1
    assert sorted(result[0]) == ["abc", "bca", "cab"] 