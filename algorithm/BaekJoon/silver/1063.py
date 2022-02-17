import sys
sys.stdin = open('input.txt', 'r')
# 왕, 돌, 움직이는 횟수
K, S, N = input().split()
N = int(N)
chess = [[0]*8 for _ in range(8)]
chess[int(K[1])-1][7-(ord(K[0])-65)] = 1
chess[int(S[1])-1][7-(ord(S[0])-65)] = 1
for i in range(8):
    print(chess[i])
# moves = [input() for _ in range(N)]
# rc = {
#     'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0),
#     'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1),
# }
#
# for move in moves:
#     r, c = rc[move]
