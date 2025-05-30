"""
문제: 괄호 유효성 검사

문자열 s가 주어질 때, 모든 괄호가 올바르게 짝지어져 있으면 True, 아니면 False를 반환하는 함수를 작성하세요.

괄호는 '(', ')', '{', '}', '[', ']' 만 사용됩니다.

예시:
>>> solution("()")
True
>>> solution("()[]{}")
True
>>> solution("(]")
False
>>> solution("([)]")
False
>>> solution("{[]}")
True

조건:
1. 입력 문자열 s의 길이는 0 이상 10,000 이하입니다.
2. 빈 문자열은 유효한 괄호로 간주합니다.
"""

def solution(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
    return not stack