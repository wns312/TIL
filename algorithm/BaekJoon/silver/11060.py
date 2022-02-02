import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
memo = [-1] * N
memo [0] = 0
for i in range(N):
    if memo[i] == -1:
        continue
    jump = arr[i]
    dis =  i + jump + 1 if i + jump + 1 < N else N
    for j in range(i, dis):
        if memo[j] == -1 or memo[j] > memo[i]:
            memo[j] = memo[i] + 1
print(memo[-1])
