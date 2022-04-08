import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
count = 0


def dfs(r, c, panel):
    global arr, N, M
    if not 0 <= r < N or not 0 <= c < M:
        return
    if arr[r][c] != panel:
        return
    if panel == '-':
        dfs(r, c+1, panel)
    if panel == '|':
        dfs(r+1, c, panel)
    arr[r][c] = 0


for r in range(N):
    for c in range(M):

        if not arr[r][c]:
            continue

        count += 1
        dfs(r, c, arr[r][c])

print(count)
