import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [1]
memo = [1]
for i in range(2, 10000000):
    if memo[-1] > N:
        break

    arr.append(arr[-1]+i)
    memo.append(arr[-1]+memo[-1])

dp = [0] * len(memo)
# 동전 문제를 먼저 풀어본 뒤 돌아오자.
# 여기 최소 사면체 개수 구하는 부분이 잘못됐음.
# ex) 70일 때 35, 20, 20, 4로 4개가 정답임. -> 어떻게 구할것인가?
for i in range(len(memo)-1, -1, -1):
    remain = N
    count = 0
    for j in range(i, -1, -1):
        count += remain // memo[j]
        remain = remain % memo[j]

    dp[i] = count
# 여기 위까지 고쳐야함
print(arr)
print(memo)
print(dp)
