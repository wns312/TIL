import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

dp = [[1]+([0] * (K-1)) for _ in range(N)]
dp[0] = [i for i in range(1, K+1)]

for r in range(1, N):
    for c in range(1, K):
        dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % 1_000_000_000

print(dp[-1][-1])
