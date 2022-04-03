import sys
sys.stdin = open('input.txt', 'r')

def get_min_withdraw(use_list, amount):
    count, remains = 1, amount

    for daily_use in use_list:
        if daily_use <= remains:
            remains -= daily_use
        else:
            count += 1
            remains = amount - daily_use
    return count


N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

s, e = max(arr), 10000*N
result = e

while s <= e:
    m = (s + e) // 2
    if max(arr) > m:
        s = m + 1
        continue
    w_count = get_min_withdraw(arr, m)
    # 틀린 것: 카운트가 작아도 최소값을 갱신해야 하는 것이 차이점.
    # 그렇다면 왜 최소값을 갱신해야 하는가?
    # 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원을 인출할 수 있다.
    # if w_count == M:
    #     result = min(m, result)
    #     e = m - 1
    # elif w_count < M:
    #     e = m - 1
    # else:
    #     s = m + 1

    # 맞은 것
    # if w_count > M:
    #     s = m + 1
    # else:
    #     result = min(m, result)
    #     e = m - 1

print(result)