"""
문제: 문자열 다루기 기본

문자열 s가 주어질 때, 다음 조건을 모두 만족하면 True, 아니면 False를 반환하는 함수를 작성하세요.

1. 문자열의 길이가 4 또는 6입니다.
2. 문자열은 숫자로만 이루어져 있습니다.

예시:
>>> solution("a234")
False
>>> solution("1234")
True
>>> solution("123456")
True
>>> solution("12345")
False

조건:
1. 입력 문자열 s의 길이는 1 이상 10,000 이하입니다.
2. s는 알파벳과 숫자로만 이루어져 있습니다.
"""

def solution(s):
    return (len(s) == 4 or len(s) == 6) & s.isdigit()