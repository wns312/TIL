import sys
sys.stdin = open('input.txt', 'r')

# 완전 이진 트리의 높이
K = int(input())
# K 는 최대 10이므로 2의 10승까지가 노드의 번호 범위가 될 수 있다
# 노드의 수 + 1인 범위
max_num = 2**K
# 중위순회의 결과물
arr = list(map(int, input().split()))
# 함수를 정의하자
levels = [list() for _ in range(K+1)]


def b_tree(height, node):
    global arr
    if node < max_num:
        b_tree(height+1, node * 2)
        levels[height].append(arr.pop(0))
        b_tree(height+1, (node * 2) +1)


b_tree(1, 1)

for i in range(1, K+1):
    print(" ".join(map(str, levels[i])))


