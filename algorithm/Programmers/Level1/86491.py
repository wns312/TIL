def solution(sizes):
    max_w, max_h = 1, 1
    for a, b in sizes:
        w, h = (a, b) if a >= b else (b, a)
        if w > max_w:
            max_w = w
        if h > max_h:
            max_h = h

    return max_w * max_h


# 최대 길이 10,000 w, h는 1 이상 1000 이하
sizes1, r1 = [[60, 50], [30, 70], [60, 30], [80, 40]], 4000
sizes2, r2 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]], 120
sizes3, r3 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]], 133

print(solution(sizes1))
print(solution(sizes2))
print(solution(sizes3))
