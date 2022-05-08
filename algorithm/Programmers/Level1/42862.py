def solution(n, lost, reserve):
    arr = [0] + ([1] * n) + [0]
    for s in lost:
        arr[s] = 0
    for s in reserve:
        arr[s] += 1

    for i in range(1, n+1):
        if arr[i]:
            continue

        if arr[i - 1] == 2:
            arr[i-1] -= 1
            arr[i] = 1
            continue

        if arr[i + 1] == 2:
            arr[i+1] -= 1
            arr[i] = 1
            continue

    return sum(1 if arr[i] else 0 for i in range(1, n+1))


n1, lost1, reserve1, r1 = 5, [2, 4], [1, 3, 5], 5
print(solution(n1, lost1, reserve1))

n2, lost2, reserve2, r2 = 5, [2, 4], [3], 4
print(solution(n2, lost2, reserve2))

n3, lost3, reserve3, r3 = 3, [3] ,[1], 2
print(solution(n3, lost3, reserve3))

