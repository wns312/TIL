import sys
sys.stdin = open('input.txt', 'r')

def comb(idx, pick, sel, arr):
    if pick == 6:
        for i in range(len(arr)):
            if sel[i]:
                print(arr[i], end=' ')
        print()
        return
    if idx == len(arr):
        return
    # 반복이 아니잖아..바보야
    sel[idx] = 1
    comb(idx+1, pick+1, sel, arr)
    sel[idx] = 0
    comb(idx + 1, pick, sel, arr)


while True:
    arr = list(map(int, input().split()))
    if len(arr) == 1 and not arr[0]:
        break
    K, S = arr[0], arr[1:]
    comb(0, 0, [0]*len(S), S)
    print()

