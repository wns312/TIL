import sys
sys.stdin = open('input.txt', 'r')

# 1 ~ 1000000
N, M = map(int, input().split())
# 1 ~ 1000000
times = list(map(int, input().split()))

s, e = 1, max(times) * M
result = e

while s <= e:
    m = (s + e) // 2
    b_count = 0

    for time in times:
        b_count += m // time

    if b_count < M:
        s = m + 1
    else:
        result = min(m, result)
        e = m - 1

print(result)
