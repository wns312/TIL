def solution(left, right):
    result = 0
    for i in range(left, right+1):
        # 약수 찾기
        d_nums = []
        for j in range(1, int(i**(1/2))+1):
            if not i % j:
                d_nums.append(j)
        d_len = len(d_nums)
        for j in range(d_len):
            d_nums.append(i//d_nums[j])
        result = result-i if len(set(d_nums)) % 2 else result+i
    return result


left1, right1, result1 = 13, 17, 43
left2, right2, result2 = 24, 27, 52

print(solution(left1, right1))
print(solution(left2, right2))

i = 10
# 약수 찾기
d_nums = []
for j in range(1, int(i ** (1 / 2)) + 1):
    if not i % j:
        d_nums.append(j)
d_len = len(d_nums)
for j in range(d_len):
    d_nums.append(i // d_nums[j])