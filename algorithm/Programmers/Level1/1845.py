def solution(nums):
    kind_count = len(set(nums))
    max_count = len(nums)//2
    return kind_count if kind_count < max_count else max_count


nums1, r1 = [3, 1, 2, 3], 2
nums2, r2 = [3, 3, 3, 2, 2, 4], 3
nums3, r3 = [3, 3, 3, 2, 2, 2], 2

print(solution(nums1))
print(solution(nums2))
print(solution(nums3))
