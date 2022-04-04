import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
numbers = [int(input()) for _ in range(T)]
max_number = max(numbers)
fibos = [0, 1]
while fibos[-1] != max_number:
    fibos.append(fibos[-1]+fibos[-2])

for i in range(T):
    if numbers[i] == 1:
        print(2)
        continue
    s, e = 0, len(fibos)
    while s <= e:
        m = (s + e) // 2
        if fibos[m] == numbers[i]:
            print(m)
            break
        if fibos[m] > numbers[i]:
            e = m - 1
        else:
            s = m + 1
