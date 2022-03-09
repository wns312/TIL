import sys
sys.stdin = open('input.txt', 'r')


memo = [2**i for i in range(25)]
N, K = map(int, input().split())


# 그냥 아예 2의 n승인 수라면 그냥 0개 출력하고 생랙해도됨 -> 시간초과때문에 이를 처리해주어야 함

for i in range(K-1):
    if N in memo:
        N = 0
        break
    left, right = 0, 24
    while left < right:
        mid = (left + right) // 2
        if memo[mid] > N:
            right = mid - 1
        elif memo[mid] < N:
            left = mid + 1
    left = left if memo[left] < N else left-1

    N -= memo[left]


left, right = 0, 24
while left < right:
    if N in memo:
        N = 0
        break
    mid = (left + right) // 2
    if memo[mid] > N:
        right = mid - 1
    elif memo[mid] < N:
        left = mid + 1
left = left+1 if memo[left] < N else left

if not N:
    print(0)
else:
    print(memo[left]-N)
