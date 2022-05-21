import sys
sys.stdin = open('input.txt', 'r')

from itertools import permutations


N, M, K = map(int, input().split())

entire_choice = 1
for i in range(N, N-M, -1):
    entire_choice *= i

arr = [i+1 for i in range(N)] # 전체 배열
picked = arr[:M]  # 뽑은 개수
r = list(permutations(arr, M)) # 전체 배열에서 M개 뽑은 리스트
r_count = 0

for i in range(len(r)):
    count = 0
    for p in picked:
        if p in r[i]:
            count += 1
    if count >= K:
        r_count += 1
print(r_count/entire_choice)
