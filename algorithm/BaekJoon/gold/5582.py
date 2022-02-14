import sys
sys.stdin = open('input.txt', 'r')

s1 = input()
s2 = input()
dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

for r in range(1, len(s1)+1):
    for c in range(1, len(s2)+1):
        if s1[r-1] == s2[c-1]:
            dp[r][c] = dp[r-1][c-1] + 1
max_v = 0
for r in range(1, len(s1)+1):
    if max(dp[r]) > max_v:
        max_v = max(dp[r])

print(max_v)
