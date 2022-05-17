import sys
sys.stdin = open('input.txt', 'r')

from collections import deque


N, K = map(int, input().split())
q = deque(list(map(int, input().split())))
robots = deque(2 * N * [False])
count = q.count(0)
time = 0
while count < K:
    # 단계 1: 오른쪽으로 이동한다
    q.appendleft(q.pop())
    robots.appendleft(robots.pop())
    # 단계 2: 로봇이 이동한다

    robots[N-1] = False

    for i in range(N-1, 0, -1):
        if robots[i-1] and not robots[i] and q[i]:
            robots[i-1] = False
            robots[i] = True
            q[i] -= 1

    robots[N-1] = False
    if q[0]:
        q[0] -= 1
        robots[0] = True

    count = q.count(0)
    time += 1

# 단계 3: 숫자를 센다
print(time)