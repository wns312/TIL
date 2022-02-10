import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

memo = [0]*(K+1)

for i in range(N):
    weight, value = map(int, input().split())

    for j in range(K, -1, -1):
        n_weight, n_value = weight+j, value+memo[j]

        if n_weight <= K and memo[n_weight] < n_value:
            memo[n_weight] = n_value

    if weight <= K and memo[weight] < value:
        memo[weight] = value

print(max(memo))
