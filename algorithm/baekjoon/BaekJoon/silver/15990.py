import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
arr = [int(input()) for _ in range(T)]
dp = list([0]*3 for i in range(max(arr)))
dp[0] = [1, 0, 0]
dp[1] = [0, 1, 0]
dp[2] = [1, 1, 1]
for i in range(3, max(arr)):
    dp[i][0] = (dp[i-1][1]+dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][0]+dp[i-2][2]) % 1000000009
    dp[i][2] = (dp[i-3][0]+dp[i-3][1]) % 1000000009

for n in arr:
    print(sum(dp[n-1])%1000000009)

# 이전 수 3개의 경우의 수를 보고, 다음 경우의 수를 구하는 것
