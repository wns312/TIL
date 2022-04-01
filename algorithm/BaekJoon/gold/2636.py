import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def calculate_cheese(arr):
    global dr, dc
    q = deque([(0, 0)])
    is_visited = [[0]*len(arr[0]) for _ in range(len(arr))]
    is_visited[0][0] = 1
    delete_set = set()

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = dr[i]+r, dc[i]+c
            if not (0 <= nr < len(arr)) or not (0 <= nc < len(arr[0])):
                continue

            if is_visited[nr][nc]:
                continue

            if arr[nr][nc]:
                delete_set.add((nr, nc))
                is_visited[nr][nc] = 1
            else:
                if not is_visited[nr][nc]:
                    q.append((nr, nc))
                    is_visited[nr][nc] = 1

    return delete_set


R, C = map(int, input().split())
arr = [[0]*(C+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(R)]+[[0]*(C+2)]
time = 0
last_left_cheese = 0

while True:
    delete_set = calculate_cheese(arr)
    if not len(delete_set):
        break

    last_left_cheese = len(delete_set)
    while delete_set:
        tr, tc = delete_set.pop()
        arr[tr][tc] = 0
    time += 1

print(time)
print(last_left_cheese)
