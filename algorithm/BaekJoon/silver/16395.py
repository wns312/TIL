import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
arr = [[1] for _ in range(N)]

for i in range(1, N):
    for j in range(1, i):
        arr[i].append(arr[i-1][j-1]+arr[i-1][j])
    arr[i].append(1)
print(arr[-1][K-1])