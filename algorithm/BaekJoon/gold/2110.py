N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

s, e = 1, 1000000000
result = s

while s <= e:
    m = (s + e) // 2
    count = 1
    last_device = houses[0]
    min_distance = e

    for p in houses:
        if p - last_device >= m:
            count += 1
            min_distance = min(min_distance, p - last_device)
            last_device = p

    if count < C:
        e = m - 1
    else:
        result = max(result, min_distance)
        s = m + 1

print(result)