import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visit = [[0]*M for _ in range(N)]
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(row, col, paper, visits):
    global dr, dc
    s = [(row, col)]
    visits[row][col] = 1
    d_size = 1
    while s:
        rr, cc = s.pop(-1)
        for i in range(4):
            nr, nc = rr+dr[i], cc+dc[i]
            if 0 <= nr < len(paper) and 0 <= nc < len(paper[0]) and not visits[nr][nc] and paper[nr][nc]:
                s.append((nr, nc))
                visits[nr][nc] = 1
                d_size += 1
    return d_size, visits


draw_cnt = 0
draw_max_size = 0

for r in range(N):
    for c in range(M):
        if not visit[r][c] and arr[r][c]:
            draw_size, visit = dfs(r, c, arr, visit)
            draw_cnt += 1
            if draw_max_size < draw_size:
                draw_max_size = draw_size

print(draw_cnt)
print(draw_max_size)
