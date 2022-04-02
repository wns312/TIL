import sys
sys.stdin = open('input.txt', 'r')
# 나무의 수, 가져가려고 하는 미터 수
N, M = map(int, input().split())
trees = list(map(int, input().split()))
s, e = 0, max(trees)
result = 0

while s <= e:
    m = (s + e) // 2
    amount = 0
    for tree in trees:
        if tree > m:
            amount += tree - m
    if amount == M:
        result = m
    if amount > M:
        s = m + 1
        if result < m:
            result = m
    else:
        e = m - 1

print(result)
