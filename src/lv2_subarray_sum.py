def subarray_sum(nums, target):
    """
    정수 리스트 nums와 정수 target이 주어질 때,
    연속된 부분 수열의 합이 target이 되는 경우의 수를 반환하세요.
    예시: nums = [1, 1, 1], target = 2 -> return 2
    """
    count = 0
    current_sum = 0
    prefix_sums = {0: 1}
    for num in nums:
        current_sum += num
        count += prefix_sums.get(current_sum - target, 0)
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
    return count 