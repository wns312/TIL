import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
arr = [int(input()) for _ in range(T)]
memo = [0] * 1000001
memo[0], memo[1], memo[2] = 1, 2, 4

for i in range(3, 1000001):
    memo[i] = (memo[i-1] % 1000000009) + (memo[i-2] % 1000000009) + (memo[i-3] % 1000000009)

for i in range(T):
    print(memo[arr[i]-1] % 1000000009)
