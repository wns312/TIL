import sys
sys.stdin = open('input.txt', 'r')

arr = input()

rear, front = [], []
for i in range(len(arr) - 1):
    tmp = arr[i:i + 2]
    if tmp == '((':
        rear.append(i)
    elif tmp == '))':
        front.append(i)

result = 0
for r_idx in rear:
    for i in range(len(front) - 1, -1, -1):
        if r_idx < front[i]:
            result += 1

print(result)