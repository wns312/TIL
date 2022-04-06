import sys
sys.stdin = open('input.txt', 'r')

N, H = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr1, arr2 = sorted([arr[_] for _ in range(0, N, 2)]), sorted([arr[_] for _ in range(1, N, 2)])
memo = [0] * H
for i in range(H):
    # 석순
    result1 = 0
    s, e = 0, (N//2)-1
    height = i+1
    while s <= e:
        m = (s + e) // 2
        if arr1[m] < height:  # 못부숨
            s = m + 1
        else:  # 부숨
            e = m - 1
            result1 = max(result1, (N//2)-e-1)

    # 종유석
    result2 = 0
    s, e = 0, (N//2)-1
    while s <= e:
        m = (s + e) // 2
        if height + arr2[m] > H:  # 부숨
            e = m - 1
            result2 = max(result2, (N // 2) -e-1)
        else:  # 못부숨
            s = m + 1

    memo[i] = result1 + result2

print(min(memo), memo.count(min(memo)))
