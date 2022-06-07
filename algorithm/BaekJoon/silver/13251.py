import sys
sys.stdin = open('input.txt', 'r')

M = int(input())
stones = list(map(int, input().split()))
K = int(input())

total_amount = sum(stones)
total_count = total_amount
for i in range(total_amount-1, total_amount-K, -1):
    total_count *= i

total_pick_count = 0

for i in range(M):
    if stones[i] < K:
        continue

    amount = stones[i]

    for j in range(stones[i]-1, stones[i]-K, -1):
        amount *= j

    total_pick_count += amount

print(total_pick_count/total_count)
