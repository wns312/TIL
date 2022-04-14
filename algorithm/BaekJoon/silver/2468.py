import sys
sys.stdin = open('input.txt', 'r')
# https://www.acmicpc.net/problem/2468

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
area_count = 1
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
def dfs(row, col, height, lands, visit_list):
    s = [(row, col)]
    while s:
        rr, cc = s.pop(-1)
        visit_list[rr][cc] = 1
        for i in range(4):
            nr, nc = rr+dr[i], cc+dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visit_list[nr][nc] and lands[nr][nc] > height:
                s.append((nr, nc))
    return visit_list


for i in range(1, 101):
    visit = [[0] * N for _ in range(N)]
    count = 0
    for r in range(N):
        for c in range(N):
            # 조건 걸기
            if not visit[r][c] and arr[r][c] > i:
                visit = dfs(r, c, i, arr, visit)
                count += 1
    if count > area_count:
        area_count = count

print(area_count)
