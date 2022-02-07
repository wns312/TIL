import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
dp = [1, 0, 3]
if N < 3:
    print(dp[N])
else:
    dp += [0 for _ in range(3, N+1)]
    for i in range(4, N+1, 2):
        dp[i] += dp[i-2] * 3 + 2
        for j in range(2, i-2, 2):
            dp[i] += dp[j] * 2

    print(dp[-1])


# https://0equal2.tistory.com/114
# https://hongcoding.tistory.com/84
