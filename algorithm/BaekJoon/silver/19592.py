import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    # 참가자 수
    N, X, Y = map(int, input().split())
    # 길이 N, 각 자동차의 평균 속력
    # 각 참가자의 속도
    arr = list(map(int, input().split()))

    my_speed = arr.pop(-1)
    max_speed = max(arr)
    # 이 조건이 내가 틀린 부분의 핵심
    # 아래 로직으로까지 넘어가는 경우에 연산이 진행되면 틀린 부분이 있는 것
    if my_speed > max_speed:
        print(0)
        continue
    time_to_win = X / max_speed

    result = -1
    s, e = 0, Y
    while s <= e:
        m = (s + e) // 2
        time = 1 if m else 0
        remain_track = X - m
        time += remain_track / my_speed
        if time > time_to_win:
            s = m+1
        else:
            if not time == time_to_win:
                result = m
            e = m-1
    print(result)

