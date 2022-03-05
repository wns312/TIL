import sys
sys.stdin = open('input.txt', 'r')

V = int(input())
arr = [list() for _ in range(V+1)]
for i in range(V-1):
    A, B = map(int, input().split())
    arr[A].append(B)
    arr[B].append(A)

stack = [(1, node) for node in arr[1]]
is_visited = [0] * (V + 1)
is_visited[1] = 1

while stack:
    parent, node = stack.pop()
    if not is_visited[node]:
        is_visited[node] = parent
        stack += [(node, son) for son in arr[node]]

for i in range(2, V+1):
    print(is_visited[i])



