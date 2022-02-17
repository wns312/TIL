import sys
sys.stdin = open('input.txt', 'r')
# 스위치 개수
N = int(input())
switches = list(map(int, input().split()))
M = int(input())
students = [list(map(int, input().split()))for _ in range(M)]

for _ in range(M):
    sex, idx = students[_]
    idx -= 1
    if sex == 1:
        for i in range(idx, N, idx+1):
            switches[i] = 0 if switches[i] else 1
    else:
        l, r = idx, idx
        while l > 0 and r < N-1:
            if switches[l-1] == switches[r+1]:
                l -= 1
                r += 1
            else:
                break
        if switches[l] != switches[r]:
            l += 1
            r -= 1
        for i in range(l, r+1):
            switches[i] = 0 if switches[i] else 1

print(" ".join(list(map(str, switches))))

