import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(100000)
N, R, Q = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N-1)]
root_nodes = [int(input()) for _ in range(Q)]
# print(N, R, Q)
# print(arr)
# print(root_nodes)
# 트리 리스트 만들기
tree = [list() for _ in range(N+1)]
for A, B in arr:
    tree[A].append(B)
    tree[B].append(A)
# print(tree)
memo = [0] * (N+1)


# 트리의 각 서브트리 계산 재귀함수 만들기
def make_sub_nodes(current_node, p_node):
    global memo
    node_sum = 1
    for child_node in tree[current_node]:
        if child_node == p_node:
            continue

        node_sum += make_sub_nodes(child_node, current_node)
    memo[current_node] = node_sum
    return node_sum


make_sub_nodes(R, -1)
# print(memo)

for node in root_nodes:
    print(memo[node])