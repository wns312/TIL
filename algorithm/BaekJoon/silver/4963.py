import sys
sys.stdin = open('input.txt', 'r')

dr = [1, -1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, 1, -1, -1, 1, -1, 1]


def dfs(row, col, land_list):
    s = [(row, col)]
    while s:
        rr, cc = s.pop(-1)
        land_list[rr][cc] = 0
        for i in range(8):
            nr, nc = rr + dr[i], cc + dc[i]
            if 0 <= nr < h and 0 <= nc < w and land_list[nr][nc]:
                s.append((nr, nc))
    return land_list


while True:
    w, h = map(int, input().split())
    if not w and not h:
        break

    lands = [list(map(int, input().split())) for _ in range(h)]
    visit = [[0]*w for _ in range(h)]
    count = 0

    for r in range(h):
        for c in range(w):
            if not visit[r][c] and lands[r][c]:
                lands = dfs(r, c, lands)
                count += 1
    print(count)
