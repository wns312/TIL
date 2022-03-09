import sys
sys.stdin = open('input.txt', 'r')

import sys
sys.setrecursionlimit(10**9)
pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except EOFError as e:
        break


def post_order(left, right):
    if left > right:
        return
    edge = right
    # 왼쪽과 오른쪽 범위 구하기

    for i in range(left+1, right+1):
        if pre_order[i] > pre_order[left]:
            edge = i-1
            break

    post_order(left+1, edge)
    post_order(edge+1, right)
    print(pre_order[left])


post_order(0, len(pre_order)-1)
