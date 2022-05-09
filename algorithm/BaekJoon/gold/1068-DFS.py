import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
D = int(input())
tree = [[] for _ in range(N)]
parent_node = arr.index(-1)

for i in range(N):
    if i == D or arr[i] == -1:
        continue
    tree[arr[i]].append(i)


def dfs(idx, tree_list):
    if not tree_list[idx]:
        return 1
    cnt = 0
    for node in tree_list[idx]:
        cnt += dfs(node, tree_list)
    return cnt


result = 0
if parent_node != D:
    result = dfs(parent_node, tree)
print(result)
