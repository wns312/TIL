import sys
from queue import PriorityQueue
sys.stdin = open('../gold/input.txt', 'r')


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 'Hing'
def dfs(r, c):
    global arr, result, N
    if not arr[r][c]:
        return
    if r == N-1 and c == N-1:
        result = 'HaruHaru'
        return
    move = arr[r][c]
    if r+move < N:
        dfs(r+move, c)
    if c + move < N:
        dfs(r, c+move)

dfs(0, 0)
print(result)

