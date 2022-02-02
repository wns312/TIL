import sys
sys.stdin = open('input.txt', 'r')

N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, M):
    arr[0][i] += arr[0][i-1]
for i in range(1, N):
    arr[i][0] += arr[i-1][0]
for r in range(1, N):
    for c in range(1, M):
        arr[r][c] += max(arr[r-1][c], arr[r][c-1])

print(arr[-1][-1])
