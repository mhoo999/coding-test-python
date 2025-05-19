"""
문제: 가장 가까운 같은 글자

문자열 s가 주어질 때, 각 위치마다 자신보다 앞에 나왔던 같은 글자가 몇 칸 앞에 있었는지 배열로 반환하는 함수를 작성하세요.  
같은 글자가 없으면 -1을 반환합니다.

예시:
>>> solution("banana")
[-1, -1, -1, 2, 2, 2]
>>> solution("foobar")
[-1, -1, 1, -1, -1, -1]
>>> solution("abacabad")
[-1, -1, 2, -1, 2, 4, 2, -1]

조건:
1. 입력 문자열 s의 길이는 1 이상 10,000 이하입니다.
2. s는 영문 소문자로만 이루어져 있습니다.
"""

def solution(s):
    last_index = {}
    result = []
    for i, char in enumerate(s):
        if char in last_index:
            result.append(i - last_index[char])
        else:
            result.append(-1)
        last_index[char] = i
    return result
