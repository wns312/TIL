import sys
sys.stdin = open('input.txt', 'r')

s1 = input()
s2 = input()
dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]


for r in range(1, len(s2)+1):
    for c in range(1, len(s1)+1):
        if s2[r-1] == s1[c-1]:
            dp[r][c] = dp[r-1][c-1] +1
        else:
            dp[r][c] = max(dp[r-1][c], dp[r][c-1])
print(dp[-1][-1])

# for r in range(1, len(s2)):
#     for c in range(1, len(s1)):
#         if s2[r-1] == s1[c-1]:
#             dp[r][c] = dp[r-1][c-1] + 1
#
for i in range(len(s2)+1):
    print(dp[i])



