import sys
sys.stdin = open('input.txt', 'r')

A, B = map(int, input().split())
og = {input(): True for _ in range(A)}
count = 0

for i in range(B):
    try:
        if og[input()]:
            count += 1
    except Exception:
        pass

print(count)