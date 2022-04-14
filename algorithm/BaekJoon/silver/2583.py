import sys
sys.stdin = open('input.txt', 'r')

N, M, K = map(int, input().split())
arr = [[1] * M for _ in range(N)]

for k in range(K):
    # 왼쪽 아래, 오른쪽 위 꼭짓점 -> x1, y2와 x2, y1을 매칭하면 된다
    x1, y1, x2, y2 = map(int, input().split())
    # 디테일은 문제보고 잡기
    for r in range(y1, y2):
        for c in range(x1, x2):
            arr[r][c] = 0


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(row, col, areas, visit_list):
    s = [(row, col)]
    visit_list[row][col] = 1
    cnt = 1
    while s:
        rr, cc = s.pop(-1)
        for i in range(4):
            nr, nc = rr+dr[i], cc+dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visit_list[nr][nc] and areas[nr][nc]:
                s.append((nr, nc))
                visit_list[nr][nc] = 1
                cnt += 1
    return cnt, visit_list


visit = [[0] * M for _ in range(N)]
results = []

for r in range(N):
    for c in range(M):
        if not visit[r][c] and arr[r][c]:
            count, visit = dfs(r, c, arr, visit)
            results.append(count)

print(len(results))
print(' '.join(list(map(str, sorted(results)))))
