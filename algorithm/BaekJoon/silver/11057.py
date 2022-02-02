import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    memo = arr[0]
    for j in range(1, 10):
        memo += arr[j]
        arr[j] = memo
print(sum(arr) % 10007)
