import sys
sys.stdin = open('input.txt', 'r')
# 전체 input
R, C = map(int, input().split())
space = [input() for _ in range(R)]
PR, PC = map(int, input().split())
# 상 우 하 좌 순서로 우선한 것을 출력
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 반사 시 전환 방향을 기록한 dict
reflect = {
    '\\': [3, 2, 1, 0],
    '/': [1, 0, 3, 2],
}

# 각각 상 우 하 좌 방향으로 갔을 때, 얼마나 갔는지를 저장하는 result 배열을 초기화
result = [0, 0, 0, 0]
for _ in range(4):
    # i는 시작 방향만 정한다
    d = _
    # 맞아서 방향을 바꾸면 d 를 바꾼다
    # 현재 좌표 : 이제 dr, dc를 더해서 새로운 위치를 정한다
    r, c = PR-1, PC-1

    # 방향 바꾸는 로직이 핵심이 될 것
    # 최대 전체 좌표 개수 까지 진행
    for i in range(R*C*2):
        if space[r][c] == 'C':
            break
        result[_] += 1

        # 새 좌표
        r, c = r + dr[d], c + dc[d]
        if not 0 <= r < R or not 0 <= c < C:
            break
        if space[r][c] == '.':
            continue

        d = reflect['/'][d] if space[r][c] == '/' else reflect['\\'][d]

max_v = max(result)
for i in range(4):
    if result[i] == max_v:
        print(['U', 'R', 'D', 'L'][i])
        print('Voyager' if max(result) >= R*C*2 else result[i])
        break

# 4 4
# ./\/
# \..\
# /../
# \/\/
# 1 1

# D
# 20