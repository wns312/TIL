import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for _ in range(T):
    moves = input()
    # 변수 초기화
    x, y, d = 0, 0, 0  # 현재 위치 기록 용도
    rx, ry = [0, 0], [0, 0]  # 범위 담는 용도
    for move in moves:
        if move == 'L' or move == 'R':
            d = (d - 1) % 4 if move == 'L' else (d + 1) % 4
        elif move == 'F' or move == 'B':
            ny, nx = (dy[d], dx[d]) if move == 'F' else (dy[(d-2)%4], dx[(d-2)%4])
            # 새로운 위치가 아니라 더하고 빼야 할 값
            x += nx
            y += ny
            if x > 0 and x > rx[1]:
                rx[1] = x
            elif x < 0 and x < rx[0]:
                rx[0] = x

            if y > 0 and y > ry[1]:
                ry[1] = y
            elif y < 0 and y < ry[0]:
                ry[0] = y

    print(abs(rx[0] - rx[1]) * abs(ry[0] - ry[1]))



