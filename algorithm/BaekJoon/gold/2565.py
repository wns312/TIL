import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lines = sorted(list(list(map(int, input().split())) for _ in range(N)))

arr = [0] * (lines[-1][0]+1)
dp = [1] + [0] * (lines[-1][0])

for i in range(N):
    arr[lines[i][0]] = lines[i][1]

for i in range(1, len(arr)):
    if arr[i] == 0:
        continue

    for j in range(1, i):
        if arr[j] < arr[i] and dp[j] > dp[i]:
            dp[i] = dp[j]

    dp[i] += 1

print(N-max(dp))
