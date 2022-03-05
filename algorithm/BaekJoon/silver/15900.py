import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list() for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    arr[A].append(B)
    arr[B].append(A)

total_height = 0
is_visited = [False] * (N + 1)
is_visited[1] = True
# 재귀 깊이때문에 스택 while로 변경
stack = [(1, son) for son in arr[1]]

while stack:
    height, node = stack.pop()
    if not is_visited[node]:
        # 방문처리
        is_visited[node] = True

        # 자식노드가 있는지 검사
        is_not_visited_nodes = False

        for son in arr[node]:
            if not is_visited[son]:
                is_not_visited_nodes = True
                break
        # 자식 노드가 있다면?
        if is_not_visited_nodes:
            for son in arr[node]:
                stack.append((height+1, son))
        # 자식 노드가 없다면 리프노드
        else:
            total_height += height

print('Yes' if total_height % 2 else 'No')
