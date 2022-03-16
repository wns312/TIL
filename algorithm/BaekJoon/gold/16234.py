from collections import deque
N, L, R = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
# 상하좌우
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
day = 0
visit = None

def bfs(row, col):
    global visit

    q = deque([(row, col)])
    union_list = [(row, col)]
    visit[row][col] = 1
    total = arr[row][col]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if not 0 <= nr < N or not 0 <= nc < N:
                continue
            if visit[nr][nc]:
                continue
            if not (L <= abs(arr[nr][nc] - arr[r][c]) <= R):
                continue

            q.append((nr, nc))
            union_list.append((nr, nc))
            visit[nr][nc] = 1
            total += arr[nr][nc]

    return union_list, total//len(union_list)

while True:

    visit = [[0]*N for _ in range(N)]
    move_exist = False

    for r in range(N):
        for c in range(N):

            if visit[r][c]:
                continue

            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]

                if not 0 <= nr < N or not 0 <= nc < N:
                    continue
                if visit[nr][nc]:
                    continue
                if not (L <= abs(arr[nr][nc]-arr[r][c]) <= R):
                    continue

                move_exist = True

                union_list, average = bfs(r, c)
                for row, col in union_list:
                    arr[row][col] = average
                break

    if not move_exist:
        break
    day += 1

print(day)