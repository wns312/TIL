import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    wear_count_dict = {}
    for i in range(N):
        _, category = input().split(' ')
        try:
            wear_count_dict[category] += 1
        except KeyError:
            wear_count_dict[category] = 2

    keys = wear_count_dict.keys()

    result = 1

    for k in keys:
        result *= wear_count_dict[k]

    print(result-1)
