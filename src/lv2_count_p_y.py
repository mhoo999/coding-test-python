"""
문제: 문자열 내 p와 y의 개수

문자열 s가 주어질 때, 'p'와 'y'의 개수가 같으면 True, 다르면 False를 반환하는 함수를 작성하세요.
대소문자는 구분하지 않습니다.

예시:
>>> solution("pPoooyY")
True
>>> solution("Pyy")
False
>>> solution("abc")
True

조건:
1. 입력 문자열 s의 길이는 1 이상 10,000 이하입니다.
2. s는 알파벳으로만 이루어져 있습니다.
3. 대소문자는 구분하지 않습니다.
"""

def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')