import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

from collections import deque
N, K = int(input()), int(input())
apples = [list(map(lambda x: int(x)-1, input().split())) for _ in range(K)]
L = int(input())
moves = [list(input().split()) for _ in range(L)]
moves = [[int(moves[_][0]), moves[_][1]] for _ in range(L)]
snake = deque()
snake.append((0, 0))
# 시작 : 뱀은 오른쪽으로 먼저 움직이고, 0, 0에서부터 시작한다
r, c, d, time = 0, 0, 0, 0
# 우하좌상
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
while True:
    # 1초 경과
    time += 1
    # 이동하게 될 좌표
    nr, nc = snake[0][0] + dr[d], snake[0][1] + dc[d]
    print(f'뱀의 위치 {nr, nc}')
    # 이동할 곳이 벽인지부터 확인하기
    if not 0 <= nr < N or not 0 <= nc < N:
        break

    # 혹시 몸통이나 꼬리에 닿았는지 확인
    if [nr, nc] in snake:
        break
    # 실제 이동 (머리)
    snake.appendleft([nr, nc])


    # 사과가 있는지 확인
    if apples and [nr, nc] in apples:
        apples.pop(apples.index([nr, nc]))  # 사과를 없애고, 길이가 늘어나므로 꼬리에서 빼지 않는다.
    else:
        snake.pop()  # 사과가 없으면 길이가 안늘어나므로 맨 뒤의 것을 하나 뺀다
    # 방향 전환 확인
    if moves and time == moves[0][0]:
        direction = moves[0][1]
        d = (d - 1) % 4 if direction == 'L' else (d+1) % 4
        moves.pop(0)


print(time)
