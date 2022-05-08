import itertools


# 순열 말고 조합을 구하는 문제
# 1. 조합 툴 사용하기
def solution(nums):
    # a) 에라토스테네스의 체 배열 만들기
    punisher = [True] * 3001
    punisher[0], punisher[1] = False, False
    for i in range(2, 3001):
        if not punisher[i]:
            continue
        for j in range(i*2, 3001, i):
            punisher[j] = False
    # b) 조합 배열 구하기
    cbnts = list(itertools.combinations(nums, 3))
    # c) 조합의 합을 구하고 그 합을 에라토스테네스의 체 배열로 소수판별한다.
    # 소수로 판별되면 1을 더해준다
    return sum(1 for i in range(len(cbnts)) if punisher[sum(cbnts[i])])


# 2. 조합 직접 구현하기
def solution(nums):
    # a) 에라토스테네스의 체 배열 만들기
    punisher = [True] * 3001
    punisher[0], punisher[1] = False, False
    for i in range(2, 3001):
        if not punisher[i]:
            continue
        for j in range(i*2, 3001, i):
            punisher[j] = False

    # b) 조합 배열 구하기 : punisher와 nums의 외부참조가 있으므로 순수함수가 아님
    def get_combination(idx, sel, total, remains):
        # 3개를 뽑았다면 소수여부 판별해서 리턴
        if sel == 3:
            return 1 if punisher[total] else 0
        # 다 뽑았는데 3개가 아닌 경우 and 이후의 모든것을 뽑아도 3개가 될 수 없는 경우
        if idx == len(nums) and sel+(len(nums)-idx) < 3:
            return 0
        a = get_combination(idx+1, sel+1, total+nums[idx], remains-nums[idx])
        b = get_combination(idx+1, sel, total, remains)
        return a+b

    return get_combination(0, 0, 0, sum(nums))


nums1, r1 = [1, 2, 3, 4], 1
nums2, r2 = [1, 2, 7, 6, 4], 4
print(solution(nums1))
print(solution(nums2))
