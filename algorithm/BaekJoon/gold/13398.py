import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
# 음수라면 음수의 최대값을 출력
if max(arr) < 0:
    print(max(arr))

# 음수가 아니라면 A가 이미 음수를 제외한 값, B를 제외할 수 있는 값으로 간주
# 각 값을 계속 가져가면서 memo에 최대값을 저장한다
else:
    A, B = 0, 0
    memo = [0] * N
    for i in range(N):
        num = arr[i]
        A = max(B, A+arr[i], 0)
        B = max(B+arr[i], 0)
        memo[i] = max(A, B)
    print(max(memo))


