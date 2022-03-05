import sys
sys.stdin = open('input.txt', 'r')

# 정점, 간선
V, E = int(input()), int(input())
arr = [list() for _ in range(V+1)]
is_visited = [False] * (V + 1)
for _ in range(E):
    A, B = map(int, input().split())
    arr[A].append(B)
    arr[B].append(A)

stack = list(arr[1])
is_visited[1] = True
while stack:

    node = stack.pop()

    if is_visited[node]:
        continue

    is_visited[node] = True
    stack += arr[node]

print(is_visited.count(True)-1)

