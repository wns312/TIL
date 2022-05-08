def solution(n):
    # n의 나머지가 1이라면?? 홀수
    # 홀수일 경우 2가 제일 작은 수
    if n % 2:
        return 2
    # n이 짝수인 경우 홀수만 고려하면 된다
    for i in range(3, n, 2):
        if n % i == 1:
            return i

n1, r1 = 3, 10
n2, r2 = 12, 11

print(solution(n1))
print(solution(n2))