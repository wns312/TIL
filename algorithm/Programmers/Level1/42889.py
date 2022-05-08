def solution(N, stages):
    total_user_cnt = len(stages)
    fail_user_idx_list = [0] * (N+1)
    for s in stages:
        if s > N:
            continue
        fail_user_idx_list[s] += 1

    # 도달한 플레이어수 구하기
    arrived_list = [total_user_cnt]
    for i in range(1, N+1):
        arrived_list.append(
            arrived_list[i - 1] - fail_user_idx_list[i - 1]
        )

    clear_per_list = [[1, 0]]
    for i in range(1, N + 1):
        clear_per_list.append(
            [((arrived_list[i]-fail_user_idx_list[i])/arrived_list[i]), i]
            # 스테이지에 도달한 사람이 없으면 실패율이 0이므로, 1을 넣어주어야 한다.
            # 스테이지에 도달한 사람이 없다면 0으로 나누게 되어 zerodivision error가 발생함
            if arrived_list[i] else [1, i]
        )
        clear_per_list[i][0] = 1-clear_per_list[i][0]

    clear_per_list = sorted(clear_per_list[1:], key=lambda x: (-x[0], x[1]))
    return [b for a, b in clear_per_list]

n1, stages1, results1 = 5, [2, 1, 2, 6, 2, 4, 3, 3], [3, 4, 2, 1, 5]
n2, stages2, results2 = 4, [4, 4, 4, 4, 4], [4, 1, 2, 3]

print(solution(n1, stages1))
print(solution(n2, stages2))
print(solution(3, [1, 1, 1]))
