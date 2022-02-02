import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]

for i in range(1, N):
    max_list = [dp[j] + dp[-1*j-1] for j in range((i+1)//2)]
    dp.append(max(max_list + [arr[i]]))
print(max(dp))
