import sys
from random import randrange
sys.stdin = open('input.txt', 'r')

# 재귀로 풀었다 결국...왜 stack을 사용한 while문에서는 못풀었을까..?
# 풀 수 없는걸까 아니면 지나치게 복잡한걸까?
# 따지고보면 visit의 진입, 다시말해 depth가 깊어지는 경우에는 True를 만들고,
# depth가 얕아지는 경우에는 False를 만들면 된다.
# 다시 말해 이전 depth에 대한 저장이 필요하다는 것
# 그렇다면 pop을 하자마자 이전 depth와 node를 알고 있고,
# 비교해 증감을 구하면 똑같이 구현이 가능하다는 말이 된다.
def dfs(idx, node_list, visit_list, depth=1):
    print(idx, depth, visit_list)
    if depth == 5:
        return True
    for n in node_list[idx]:
        if not visit_list[n]:
            visit_list[n] = 1
            r = dfs(n, node_list, visit_list, depth+1)
            visit_list[n] = 0
            if r:
                return True
    return False


N, M = map(int, input().split())
nodes = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

result = 0

for i in range(N):
    visit = [0] * N
    visit[i] = 1
    is_row = dfs(i, nodes, visit)
    if is_row:
        result = 1
        break

print(result)

