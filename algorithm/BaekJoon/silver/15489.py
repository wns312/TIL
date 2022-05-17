import sys
sys.stdin = open('input.txt', 'r')

R, C, W = map(int, input().split())
N = R+W-1
arr = [[1] for _ in range(N)]

# 파스칼 계산부
for i in range(1, N):
    for j in range(1, i):
        arr[i].append(arr[i-1][j-1]+arr[i-1][j])
    arr[i].append(1)

# 부분집합 계산부
count = 0

for r in range(R-1, R+W-1):
    for c in range(C-1, C+(r-R+1)):
        count += arr[r][c]

print(count)
