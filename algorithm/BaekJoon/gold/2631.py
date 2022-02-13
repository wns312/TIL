import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [1] + [0] * (N-1)

# 가잔 긴 증가하는 부분수열
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
print(N-max(dp))
