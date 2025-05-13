"""
문제: 두 문자열이 애너그램인지 확인하기

두 개의 문자열 s와 t가 주어졌을 때, 두 문자열이 애너그램(anagram) 관계이면 True, 아니면 False를 반환하는 함수를 작성하세요.

애너그램이란, 두 문자열에 포함된 문자의 종류와 개수가 모두 같으면 성립합니다. (순서는 달라도 됨)

예시:
>>> solution("listen", "silent")
True
>>> solution("hello", "bello")
False
>>> solution("anagram", "nagaram")
True
>>> solution("rat", "car")
False

조건:
1. 입력 문자열 s와 t는 영문 소문자와 숫자로만 이루어져 있습니다.
2. 두 문자열의 길이는 1 이상 10,000 이하입니다.
"""

def solution(s, t):
    return sorted(s) == sorted(t)