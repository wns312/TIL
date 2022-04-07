from collections import deque


def bfs(s, e):
    global arr
    visited = [False] * (N+1)
    q = deque(arr[s])
    visited[s] = True
    while q:
        node, distance = q.popleft()
        visited[node] = True
        if node == e:
            return distance

        for n, d in arr[node]:
            if not visited[n]:
                q.append((n, d+distance))


N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b, d = map(int, input().split())
    arr[a].append((b, d))
    arr[b].append((a, d))

for _ in range(M):
    a, b = map(int, input().split())
    print(bfs(a, b))


