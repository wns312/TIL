import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
# 딱 안맞아 떨어지더라도, 크면서 가장 근접한 제곱근을 찾아야 한다
s,e = 1, N
result = 0
while s <= e:
    m = (s + e) // 2
    M = m ** 2
    if M == N:
        result = m
        break
    if M > N:
        e = m - 1
        result = m
    else:
        s = m + 1

print(result)