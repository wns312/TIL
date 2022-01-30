import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
memo = [1] * N

for i in range(1, N):
    # 조건을 만족하는 경우가 없다면 빈 배열에서 max를 찾으므로 [0] 을 더해준다.
    memo[i] += max([0] + [memo[j] for j in range(0, i) if arr[j] < arr[i]])

print(max(memo))


