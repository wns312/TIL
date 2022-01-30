import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
memo = [[-1]*N for _ in range(N)]


def dfs(r=0, c=0):
    if r == N-1 and c == N-1:
        return 1
    if memo[r][c] == -1:
        memo[r][c] = 0
        nr, nc = arr[r][c] + r, arr[r][c] + c
        if nr < N:
            memo[r][c] += dfs(nr, c)
        if nc < N:
            memo[r][c] += dfs(r, nc)
    return memo[r][c]


print(dfs())

# 오른쪽 먼저 진행한다고 가정했을 때
# 화살표 행 세번째 1에 memo[r][nc] == -1 조건이 걸려 있다면
# 아예 진행을 하지 않을 뿐만 아니라 네번째 1의 값을 더하지도 않게 됨
# 그 이유 때문에 틀린 것
# 2011
# 0011 <--
# 0000
