import sys
sys.stdin = open('input.txt', 'r')

numbers = [int(input())]
while numbers[-1]:
    numbers.append(int(input()))
numbers = numbers[:-1]
# 알약 경우의 수 만들기
pills = [[0]*31 for _ in range(31)]
pills[0] = [0] + ([1] * 30)

for r in range(1, 31):
    for c in range(r, 31):
        pills[r][c] = pills[r-1][c] + pills[r][c-1]

for n in numbers:
    print(pills[n][n])
