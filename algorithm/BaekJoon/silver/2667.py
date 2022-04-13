import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
counts = []
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for r in range(N):
    for c in range(N):
        if arr[r][c]:
            s = [(r, c)]
            count = 0
            while s:
                rr, cc = s.pop(-1)
                if arr[rr][cc]:
                    count += 1
                    arr[rr][cc] = 0

                for i in range(4):
                    nr, nc = rr+dr[i], cc+dc[i]
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]:
                        s.append((nr, nc))

            counts.append(count)

counts.sort()

print(len(counts))

for i in range(len(counts)):
    print(counts[i])
