N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
result = [1000000000, 1000000000]
for i in range(N):
    A = numbers[i]
    s, e = i + 1, N - 1
    # 20억: 최대 차이
    dif = [1000000000, 1000000000]

    while s <= e:
        m = (s + e) // 2
        if abs(A + numbers[m]) < abs(sum(dif)):
            dif = [A, numbers[m]]
        if A + numbers[m] == 0:
            break
        elif A + numbers[m] < 0:
            s = m + 1
        else:
            e = m - 1

    # 이 조합이 기존 result보다 작다면 result 갱신
    if abs(sum(result)) > abs(sum(dif)):
        result = dif

    # 0인 경우 탈출
    if not sum(result):
        break
print(' '.join(list(map(str, result))))