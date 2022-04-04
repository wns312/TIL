import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
c_count = sum([sum(arr[_]) for _ in range(N)])
s, e = 0, 10000000
result = 10000000

while s <= e:
    # 시간
    m = (s + e) // 2
    count = 0
    for r in range(N):
        for c in range(N):
            count += arr[r][c] if m > arr[r][c] else m
    if count >= c_count / 2:
        result = min(m, result)
        e = m - 1
    else:
        s = m + 1

print(result)
