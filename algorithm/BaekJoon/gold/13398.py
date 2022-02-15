import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
dp[0] = arr[0]
max_v = 0
for i in range(1, N):
    dp[i] = arr[i] if arr[i] > dp[i-1]+arr[i] else dp[i-1]+arr[i]
    if dp[i] > max_v:
        max_v = dp[i]

for i in range(1, N):
    if dp[i] < dp[i-1] and dp[i-1] > 0:

        for j in range(i+1, N):
            if dp[j] + dp[i-1] < 0:
                break
            if dp[j] + dp[i-1] > max_v:
                max_v = dp[j] + dp[i-1]
print(max_v)





print(dp)
