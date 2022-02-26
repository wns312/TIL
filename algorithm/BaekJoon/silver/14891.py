import sys
sys.stdin = open('input.txt', 'r')
# 기어
gears = [input() for _ in range(4)]
# 회전 횟수
K = int(input())
# 12시 방향 인덱스
indexes = [0, 0, 0, 0]

for _ in range(K):
    # 회전시킬 톱니, 회전시킬 방향 : 1은 시계방향, -1은 반시계 방향
    p, d = map(int, input().split())
    # 실제 배열 인덱스와 맞춰주기
    p -= 1
    # 움직인다는 방향과는 별개로, 실제 인덱스는 시계방향일 때 왼쪽, 반시계일 때 오른쪽이므로 반대로 바꿔준다
    d *= -1
    # 왼쪽과 오른쪽 바뀌어야 할 범위를 지정할 것
    l, r = p, p

    for i in range(p-1, -1, -1):
        # 극이 다르면 회전한다
        c_idx = indexes[i+1]
        l_idx = indexes[i]
        # 극이 같으면 안움직이므로 탈출
        if gears[i+1][(c_idx-2) % 8] == gears[i][(l_idx+2) % 8]:
            break
        l = i

    for i in range(p+1, 4):
        c_idx = indexes[i-1]
        r_idx = indexes[i]

        if gears[i-1][(c_idx + 2) % 8] == gears[i][(r_idx - 2) % 8]:
            break
        r = i

    # indexes[p] = (indexes[p] + d) % 8
    for i in range(l, r+1):
        indexes[i] = (indexes[i] + (d * -1)) % 8 if (i + p) % 2 else (indexes[i] + d) % 8

print(int(gears[0][indexes[0]])+(int(gears[1][indexes[1]])*2)+(int(gears[2][indexes[2]])*4)+(int(gears[3][indexes[3]])*8))
