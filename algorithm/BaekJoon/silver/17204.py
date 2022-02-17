import sys
sys.stdin = open('input.txt', 'r')

N, target = map(int, input().split())
arr = [int(input()) for _ in range(N)]
cnt = 0
idx = 0
for i in range(N+1):
    next_p = arr[idx]
    cnt += 1
    if next_p == target:
        break
    idx = next_p
print(-1 if cnt >= N else cnt)