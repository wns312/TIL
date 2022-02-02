import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [-1] * (K + 1)
dp[0] = 0
for i in range(1, K+1):
    l = [dp[i-coin] for coin in coins if i-coin >= 0 and dp[i-coin] != -1]
    if l:
        dp[i] = min(l)+1
print(dp[-1])
