import sys
sys.stdin = open('input.txt', 'r')

# 사실 모양이 반복되기 때문에 미리 모양을 구해놓으면
# 더이상 계산하지 않고 나머지 연산으로 처리가 가능
# 하지만 통과했기 때문에 굳이 고치지 않을 것


R, C, N = map(int, input().split())
arr = [list(input()) for i in range(R)]
arr = [[2 if _ == 'O' else 0 for _ in l] for l in arr]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

time = 2
while time <= N:
    time += 1

    # 짝수 시간에 폭탄 설지
    if time % 2:
        arr = [[1 if _ == 2 else 3 for _ in l]for l in arr]
    else:
        # 폭탄이 터지는 타이밍으로 상하좌우가 다 터져야 한다.
        for r in range(R):
            for c in range(C):
                if arr[r][c] == 1:
                    for i in range(4):
                        nr, nc = r+dr[i], c+dc[i]
                        if 0 <= nr < R and 0 <= nc < C:
                            arr[nr][nc] = 0 if arr[nr][nc] == 3 else arr[nr][nc]
                    arr[r][c] = 0

        for r in range(R):
            for c in range(C):
                if arr[r][c] == 3:
                    arr[r][c] -= 1


for i in range(R):
    result = ''.join(['O' if l else '.' for l in arr[i]])
    print(result)


