import sys
sys.stdin = open('input.txt', 'r')


def no2(row, col, direction):
    global dr, dc, space

    for i in range(1, 5):
        nr, nc = row + dr[(direction-i) % 4], col + dc[(direction-i) % 4]
        # 1) 왼쪽이 청소가 안되어 있다면?
        if not space[nr][nc]:
            # 방향전환 후 한칸 전진
            # 새로운 로봇의 방향과 위치와 몇번으로 되돌아갈지를 리턴한다
            return nr, nc, (direction-i) % 4, 1
        # 2) 벽이거나 공간이 없다면?
        elif not 0 <= nr < N or not 0 <= nc < M:
            return r, c, (direction-i) % 4, 2

    # 네방향 모두 청소되어 있거나 벽인 경우에는 한칸 후진 후 2번으로
    nr, nc = row + dr[(2 + direction) % 4], col + dc[(2 + direction) % 4]
    # 후진도 불가능한 경우
    if not 0 <= nr < N or not 0 <= nc < M or space[nr][nc] == 1:
        return nr, nc, direction, -1
    # 후진이 가능한 경우
    return nr, nc, direction, 2


N, M = map(int, input().split())
r, c, d = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
count = 0
is_working = True

while is_working:
    # 1. 현재 위치를 청소한다
    if not space[r][c]:
        space[r][c] = 2
        count += 1
    # 왼 방향 부터 인접한 곳 탐색
    while True:
        r, c, d, destination = no2(r, c, d)
        if destination == 1:
            break
        elif destination == 2:
            continue
        else:
            is_working = False
            break

print(count)
