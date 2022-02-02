import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [1]
memo = [1]

for i in range(2, 10000000):
    if arr[-1]+i + memo[-1] > N:
        break
    arr.append(arr[-1]+i)
    memo.append(arr[-1]+memo[-1])


dp = [-1] * (N+1)
dp[0] = 0

for i in range(1, (N+1)):
    l = []
    for cnt in memo:
        if i-cnt >= 0 and dp[i-cnt] != -1:
            l.append(dp[i-cnt])
    if l:
        dp[i] = min(l)+1

print(dp[-1])
