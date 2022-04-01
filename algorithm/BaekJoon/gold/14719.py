import sys
sys.stdin = open('input.txt', 'r')

H, W = map(int, input().split())
arr = list(map(int, input().split()))
water_blocks = 0
for i in range(1, H+1):
    s, e = W, 0
    for j in range(W):
        if arr[j] >= i:
            s = j
            break
    for j in range(W-1, 0, -1):
        if arr[j] >= i:
            e = j
            break

    for j in range(s, e+1):
        if arr[j] < i:
            water_blocks += 1
print(water_blocks)
