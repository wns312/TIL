import sys
sys.stdin = open('input.txt', 'r')
# 정점의 개수 N, 간선의 개수 M

N, M = map(int, input().split())
visit = [0] * (N+1)
nodes = [list() for _ in range(N+1)]

for _ in range(M):
    # 간선의 양 끝점 u, v
    u, v = map(int, input().split())
    nodes[u].append(v)
    nodes[v].append(u)


def dfs(node, node_list, visited):
    s = [node]
    while s:
        n = s.pop(-1)
        if not visited[n]:
            visited[n] = 1
            for nn in node_list[n]:
                s.append(nn)
    return visited


count = 0
for i in range(1, N+1):
    if not visit[i]:
        visit = dfs(i, nodes, visit)
        count += 1

print(count)
