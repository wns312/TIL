import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N, M, V = map(int, input().split())
nodes = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

for i in range(N+1):
    nodes[i].sort()

d_result, b_result = list(), list()
d_visit = [0] * (N+1)
b_visit = [0] * (N+1)
def dfs(node):
    global nodes, d_result, d_visit

    s = deque([node])
    while s:
        n = s.pop()
        if not d_visit[n]:
            d_visit[n] = 1
            d_result.append(n)
            for nn in range(len(nodes[n])-1, -1, -1):
                s.append(nodes[n][nn])

def bfs(node):
    global nodes, b_result, b_visit

    q = deque([node])
    while q:
        n = q.popleft()
        if not b_visit[n]:
            b_visit[n] = 1
            b_result.append(n)
            for nn in nodes[n]:
                q.append(nn)


dfs(V)
bfs(V)
print(' '.join(map(str, d_result)))
print(' '.join(map(str, b_result)))

