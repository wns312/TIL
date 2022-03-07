import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
r_tree = list(map(int, input().split())) # 각 노드의 부모 노드 정보
tree = [list() for _ in range(N)]
delete_node = int(input())
r_node = None
for i in range(N):
    parent = r_tree[i]

    # 부모가 없는, 루트노드라면
    if parent == -1:
        r_node = i
        continue
    # 삭제할 노드라면 자식 노드 목록에서 제외
    if delete_node == i:
        continue
    tree[parent].append(i)
# 삭제할 노드의 연결점을 없앤다
tree[delete_node] = []
# 루트 노드의 자식들을 스택에 넣고 dfs를 돌린다
stack = tree[r_node]

count = 0

# 루트노드가 리프노드인 경우 고려
if not stack:
    count = 1

while stack:
    node = stack.pop()

    if not tree[node]:
        count += 1

    stack += tree[node]

# 루트 노드를 삭제하는 경우를 고려
if r_node == delete_node:
    count = 0

print(count)
