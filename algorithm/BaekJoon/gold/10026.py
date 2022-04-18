import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
arr = [list(input()) for _ in range(N)]
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
R, C = len(arr), N


# 그냥 단순하게 DFS를 두개짜자. 귀찮으니까
def dfs_for_ord(row, col, draws, visits):
    s = [(row, col)]
    s_color = draws[row][col]
    visits[row][col] = 1
    while s:
        rr, cc = s.pop(-1)
        for i in range(4):
            nr, nc = rr+dr[i], cc+dc[i]
            if (
                    0 <= nr < len(draws)
                    and 0 <= nc < len(draws[0])
                    and not visits[nr][nc]
                    and draws[nr][nc] == s_color
            ):
                s.append((nr, nc))
                visits[nr][nc] = 1
    return visits


def dfs(row, col, draws, visits):
    s = [(row, col)]
    s_colors = ['R', 'G'] if draws[row][col] != 'B' else ['B']
    visits[row][col] = 1
    while s:
        rr, cc = s.pop(-1)
        for i in range(4):
            nr, nc = rr+dr[i], cc+dc[i]
            if (
                    0 <= nr < len(draws)
                    and 0 <= nc < len(draws[0])
                    and not visits[nr][nc]
                    and draws[nr][nc] in s_colors
            ):
                s.append((nr, nc))
                visits[nr][nc] = 1
    return visits


visit, visit_for_ord = [[0] * C for _ in range(R)], [[0] * C for _ in range(R)]
count, count_for_ord = 0, 0

for r in range(R):
    for c in range(C):
        if not visit_for_ord[r][c]:
            visit_for_ord = dfs_for_ord(r, c, arr, visit_for_ord)
            count_for_ord += 1

        if not visit[r][c]:
            visit = dfs(r, c, arr, visit)
            count += 1

print(count_for_ord, count)
