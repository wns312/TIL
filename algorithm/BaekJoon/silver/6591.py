import sys
sys.stdin = open('input.txt', 'r')

# 이항 쇼다운이라고 하지만, 그냥 조합 문제
# 시간초과 때문에 실제 계산처럼 다루어 주어야 함

# 여기서
# n-r과 r 중 큰 숫자만큼만 분자를 계산해주고, (n-r, r 중 큰 수와 약분한 결과만 계산)
# n-r과 r 중 작은 숫자만큼만 분모를 계산해준다 (n-r, r 중 큰 수는 약분 되었으므로)

while True:
    N, R = map(int, input().split())
    if not N and not R:
        break
    a, b = 1, 1

    for i in range(N, max(N-R, R), -1):
        a *= i
    for i in range(2, min(N-R, R)+1):
        b *= i
    print(a // b)


