import sys
sys.stdin = open('input.txt', 'r')

R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# 삭제 대상을 담을 배열
remove_list = []

for r in range(R):
    for c in range(C):
        # 땅 이라면 상 하 좌 우 확인
        if maps[r][c] == 'X':
            count = 0  # 상 하 좌 우 바다 개수 카운트

            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]  # 상 하 좌 우

                # 바다 라면?
                if (
                    not 0 <= nr < R or
                    not 0 <= nc < C or
                    maps[nr][nc] == '.'
                ):
                    count += 1  # 바다 이므로 바다 카운트 + 1
            # 바다가 3면 이상 이라면? 삭제 대상에 추가 한다
            if count >= 3:
                remove_list.append((r, c))

# 삭제 대상 소거
for r, c in remove_list:
    maps[r][c] = '.'

# 시작과 끝점 먼저 추정 후 출력을 잘라서 하기
rs, re, cs, ce = 0, R-1, 0, C-1

# 그냥 네방향 한번씩 돌려서 찾기
for r in range(R):
    if 'X' in maps[r]:
        break
    rs += 1

for r in range(R-1, -1, -1):
    if 'X' in maps[r]:
        break
    re -= 1

for c in range(C):
    is_land = False
    for r in range(R):
        if maps[r][c] == 'X':
            is_land = True
            break

    if is_land:
        break
    cs += 1

for c in range(C-1, -1, -1):
    is_land = False
    for r in range(R):
        if maps[r][c] == 'X':
            is_land = True
            break

    if is_land:
        break
    ce -= 1

for r in range(rs, re+1):
    print(''.join(maps[r][cs:ce+1]))






