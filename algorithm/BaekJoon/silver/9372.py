import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    for i in range(M):
        input()
    print(N-1)