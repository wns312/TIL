import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    docu_q = list(map(int, input().split()))
    docu_info_q = [False] * N
    docu_info_q[M] = True
    count = 0
    while True:
        priority = docu_q.pop(0)
        is_target = docu_info_q.pop(0)
        if priority >= max(docu_q+[-1]):
            count += 1
            if is_target:
                break
        else:
            docu_q.append(priority)
            docu_info_q.append(is_target)
    print(count)

