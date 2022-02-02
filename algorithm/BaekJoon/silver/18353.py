import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
arr = list(map(int, input().split()))
dp = [0] * T
for i in range(T):
    max_num = 0
    for j in range(i):
        if arr[j] > arr[i] and dp[j] > max_num:
            max_num = dp[j]
    dp[i] = max_num + 1
print(T-max(dp))