def solution(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))


a1, b1, r1 = [1, 2, 3, 4], [-3, -1, 0, 2], 3
a2, b2, r2 = [-1, 0, 1], [1, 0, -1], -2
print(solution(a1, b1))
print(solution(a2, b2))