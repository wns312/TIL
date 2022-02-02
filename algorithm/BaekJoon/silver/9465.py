import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(T):
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    dp1 = [arr1[0]]
    dp2 = [arr2[0]]
    for i in range(1, N):
        if i == 1:
            v1, v2 = dp2[-1], dp1[-1]
        else:
            v1 = max(dp2[-1], dp2[-2])
            v2 = max(dp1[-1], dp1[-2])
        dp1.append(v1+arr1[i])
        dp2.append(v2+arr2[i])

    print(max([dp1[-1], dp2[-1]]))

