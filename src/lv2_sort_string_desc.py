"""
문제: 문자열 내림차순으로 배치하기

문자열 s가 주어질 때, 대문자는 소문자보다 작은 것으로 간주하여 내림차순으로 정렬한 문자열을 반환하는 함수를 작성하세요.

예시:
>>> solution("Zbcdefg")
"gfedcbZ"
>>> solution("aAbBcC")
"cbaCBA"
>>> solution("HelloWorld")
"WroolllHe"

조건:
1. 입력 문자열 s의 길이는 1 이상 10,000 이하입니다.
2. s는 영문 대소문자로만 이루어져 있습니다.
3. 대문자는 소문자보다 작은 것으로 간주합니다.
"""

def solution(s):
    return ''.join(sorted(s, key=lambda x: (x.islower(), x), reverse=True))