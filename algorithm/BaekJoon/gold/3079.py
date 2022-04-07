# N, M = 2, 6
# arr = [7, 10]
N, M = 7, 10
arr = [3, 8, 3, 6, 9, 2, 4]
# N, M = map(int, input().split())
# arr = [int(input()) for _ in range(N)]
arr.sort()
s, e = 1, arr[0]*M
result = e
while s <= e:
    m = (s + e) // 2
    count = 0

    for i in range(N):
        count += m // arr[i]

    if count >= M:
        result = min(m, result)
        e = m - 1
    else:
        s = m + 1

print(result)
