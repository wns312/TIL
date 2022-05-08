def solution(absolutes, signs):
    return sum(
        absolutes[i]
        if signs[i] else (absolutes[i] * -1)
        for i in range(len(absolutes))
    )


absolute1 = [4, 7, 12]
signs1 = [True, False, True]
print(solution(absolute1, signs1))
r1 = 9

absolute2 = [1, 2, 3]
signs2 = [False, False, True]
r2 = 0
print(solution(absolute2, signs2))
