import sys
sys.stdin = open('input.txt', 'r')
N, M = map(int, input().split())
arr = sorted([int(input()) for _ in range(M)], reverse=True)
min_price, max_profit = arr[0], arr[0]
for i in range(1, min(N, M)):
    price, profit = arr[i], arr[i] * (i+1)
    if max_profit <= profit:
        max_profit = profit
        min_price = price
print(min_price, max_profit)
