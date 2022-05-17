import sys
sys.stdin = open('input.txt', 'r')

def get_combination_count(n, r):
    n_pac, nr_pac, r_pac = 1, 1, 1
    nr = n-r
    for i in range(2, n+1):
        n_pac *= i
    for i in range(2, r+1):
        r_pac *= i
    for i in range(2, nr+1):
        nr_pac *= i
    return n_pac // (r_pac * nr_pac)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    result = get_combination_count(M, N)
    print(result)
