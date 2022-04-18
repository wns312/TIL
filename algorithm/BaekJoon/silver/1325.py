import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
nodes = [[] for _ in range(N+1)]

# 단방향 트리같음
for m in range(M):
    a, b = map(int, input().split())
    nodes[b].append(a)


def dfs(s_node, node_list):
    visit_list = [0] * (N + 1)
    s = deque([s_node])
    count = 1
    visit_list[s_node] = 1
    while s:
        p_node = s.pop()

        for n in node_list[p_node]:
            if not visit_list[n]:
                s.append(n)
                visit_list[n] = 1
                count += 1

    return count


r_count = 1
r_list = []

for i in range(N+1):
    count = 1
    if nodes[i]:
        count = dfs(i, nodes)
    if count > r_count:
        r_count = count
        r_list = [i]
    elif count == r_count:
        r_list.append(i)

print(*sorted(r_list))
