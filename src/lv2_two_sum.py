"""
문제: 두 수의 합

정수로 이루어진 리스트 nums와 정수 target이 주어질 때, nums에서 두 수를 더해 target이 되는 서로 다른 인덱스 쌍을 찾아 해당 인덱스를 리스트로 반환하는 함수를 작성하세요. (항상 정답이 존재한다고 가정)

예시:
>>> solution([2, 7, 11, 15], 9)
[0, 1]
>>> solution([3, 2, 4], 6)
[1, 2]
>>> solution([3, 3], 6)
[0, 1]

조건:
1. 입력 리스트 nums의 길이는 2 이상 10,000 이하입니다.
2. 같은 원소를 두 번 사용할 수 없습니다.
3. 정답이 여러 개일 경우, 아무 쌍이나 반환해도 됩니다.
"""

def solution(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                return [i, j]

    pass 