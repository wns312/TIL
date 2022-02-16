import sys
sys.stdin = open('input.txt', 'r')

M, N = map(int, input().split())
place = [[0] * M for _ in range(M)]
# 아래를 보고 있는 것과 같음
# turn 0 이면 증가, turn 1 이면 감소
drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
d, nr, nc = 0, 0, 0
orders = [tuple(input().split()) for _ in range(N)]
result = True
for order, n in orders:
    if order == 'MOVE':
        nr += drc[d][0] * int(n)
        nc += drc[d][1] * int(n)

        if not 0 <= nr < M or not 0 <= nc < M:
            result = False
            break
    else:
        d = (d - 1) % 4 if int(n) else (d + 1) % 4

print(f'{nr} {nc}' if result else -1)

