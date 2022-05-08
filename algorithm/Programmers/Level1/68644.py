import itertools

def solution(numbers):
    combs = list(itertools.combinations(numbers, 2))
    return sorted(list({sum(comb) for comb in combs}))


print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))