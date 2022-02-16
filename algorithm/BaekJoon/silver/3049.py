import sys
sys.stdin = open('input.txt', 'r')

N, B = map(int, input().split())
str1 = list(input())
str2 = list(input())
str1 = [(s, 'r') for s in str1]
str2 = [(s, 'l') for s in str2]
T = int(input())

string = str1[::-1]+str2

for _ in range(T):
    i = 0
    while i < len(string)-1:
        if string[i][1] == 'r' and string[i+1][1] == 'l':
            string[i], string[i+1] = string[i+1], string[i]
            i += 2
        else:
            i += 1

print(''.join([s[0] for s in string]))



