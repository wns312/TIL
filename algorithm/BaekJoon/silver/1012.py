import sys
sys.stdin = open('input.txt', 'r')

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(r, c, lands, visits):
    s = [(r, c)]
    while s:
        row, col = s.pop(-1)
        if not visits[row][col]:
            visits[row][col] = 1
            for i in range(4):
                nr, nc = row + dr[i], col + dc[i]
                if 0 <= nr < N and 0 <= nc < M and lands[nr][nc]:
                    s.append((nr, nc))
    return visits


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1


    count = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] and not visit[r][c]:
                visit = dfs(r, c, arr, visit)
                count += 1
    print(count)
