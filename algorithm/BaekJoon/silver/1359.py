import sys
sys.stdin = open('input.txt', 'r')


# p_count: 뽑은 카운트, d_count: 목표로 하는 뽑기 카운트
# dc_count: 겹쳐야 하는 개수
def perm(picked, p_count, d_count, dc_count):
    if p_count == d_count:
        if picked[:d_count].count(True) >= dc_count:
            return 1
        return 0

    count = 0
    for i in range(len(picked)):
        if not picked[i]:
            picked[i] = True
            count += perm(picked, p_count+1, d_count, dc_count)
            picked[i] = False
    return count


N, M, K = map(int, input().split())

entire_choice = 1
for i in range(N, N-M, -1):
    entire_choice *= i

picked = [False] * N

r_count = perm(picked, 0, M, K)

print(r_count/entire_choice)
