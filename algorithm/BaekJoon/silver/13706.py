import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
s, e = 1, N
while s < e:
    m = (s+e)//2
    print(m, s, e)
    if m**2 == N:
        e = m
        break

    if m**2 < N:
        s = m + 1
    else:
        e = m - 1
print(e)