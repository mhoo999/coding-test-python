"""
문제: 애너그램 그룹화

문자열 배열이 주어졌을 때, 서로 애너그램인 단어들을 그룹화하여 반환하는 함수를 작성하세요.
애너그램이란 단어의 글자들을 재배열해서 다른 뜻을 가진 단어를 만들 수 있는 단어를 의미합니다.

예시:
>>> solution(["eat", "tea", "tan", "ate", "nat", "bat"])
[
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
]

>>> solution([""])
[[""]]

>>> solution(["a"])
[["a"]]

조건:
1. 입력된 문자열은 모두 소문자 알파벳으로만 이루어져 있습니다.
2. 각 그룹 내의 단어들은 알파벳 순서로 정렬되어야 합니다.
3. 그룹들의 순서는 상관없습니다.
"""

def solution(words):
    anagram_groups = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]

    for group in anagram_groups.values():
        group.sort()
    
    return list(anagram_groups.values())
    