import sys
sys.stdin = open('input.txt', 'r')

T = int(input())  # 문제의 수
for _ in range(T):  # 문제의 수만큼 반복
    N = int(input())  # 동전의 개수
    coins = list(map(int, input().split()))  # 동전의 종류
    R = int(input())  # 만들어야 하는 수
    dp = [1] + [0] * R
    dp[0] = 1
    for coin in coins:
        for i in range(1, R + 1):
            if i >= coin:
                dp[i] += dp[i - coin]
    print(dp[-1])



