import sys
sys.stdin = open('input.txt', 'r')

n, r = map(int, input().split())
nr = n-r
# nCm을 출력한다
n_pac, r_pac, nr_pac = 1, 1, 1
for i in range(2, n+1):
    if i <= nr:
        nr_pac *= i
    if i <= n:
        n_pac *= i
    if i <= r:
        r_pac *= i
print(n_pac//(nr_pac*r_pac))
