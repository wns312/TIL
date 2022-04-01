import sys
sys.stdin = open('input.txt', 'r')

T, W = map(int, input().split())
arr = [int(input()) for _ in range(T)]
memo = [[[0, W]], []]
for i in range(T):
    position = arr[i] - 1
    # 만약 내가 서있는 위치가 떨어지는 위치라면, 그대로 먹은 개수 1 증가시켜준다
    for j in range(len(memo[position])):
        memo[position][j][0] += 1
    opposite = (position + 1) % 2
    for j in range(len(memo[opposite])):
        # 남은 이동횟수가 없다면 패스
        if not memo[opposite][j][1]:
            continue
        # 이동시 먹게 될 숫자
        w_eat = memo[opposite][j][0] + 1
        # 이동시 남은 횟수
        w_move = memo[opposite][j][1] - 1
        can_be_added = True
        for k in range(len(memo[position])):
            # 결과적으로 개수도 적고 이동횟수도 적은게 들어가 있을 수 있다
            # 기존에 들어있던 메모가 들어갈 값보다 둘 다 적은 경우이기 때문.
            # 이 경우에는 큐를 사용하면 pop하면 될 것이라고 생각하긴 하는데, 굳이 바꿀 필요는 없어보임
            if w_eat <= memo[position][k][0] and w_move <= memo[position][k][1]:
                can_be_added = False
                break

        if can_be_added:
            memo[position].append([w_eat, w_move])

max_jadu = max([n for n, r in memo[0]] + [n for n, r in memo[1]])
print(max_jadu)
