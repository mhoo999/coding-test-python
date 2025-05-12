"""
문제: 가장 긴 중복 없는 부분 문자열의 길이

문자열 s가 주어졌을 때, 중복된 문자가 없는 가장 긴 부분 문자열의 길이를 반환하는 함수를 작성하세요.

예시:
>>> solution("abcabcbb")
3   # "abc"
>>> solution("bbbbb")
1   # "b"
>>> solution("pwwkew")
3   # "wke"
>>> solution("")
0

조건:
1. 입력 문자열 s는 영문 소문자와 숫자로만 이루어져 있습니다.
2. 부분 문자열은 연속된 문자로 이루어져야 합니다.
"""

#슬라이딩 윈도우 알고리즘을 사용하여 풀이

def solution(s):
    seen = {}
    start = 0
    max_len = 0
    max_substr = ""

    for end in range(len(s)):
        char = s[end]
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = end

        if end - start + 1 > max_len:
            max_len = end - start + 1
            max_substr = s[start:end+1]
    
    return max_len
