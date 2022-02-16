import sys
sys.stdin = open('input.txt', 'r')

N, L = map(int, input().split())
lights = [list(map(int, input().split()))for _ in range(N)]
position = 0
T = 0
for _ in range(N):
    P, R, G = lights[0]
    T += P - position  # 신호등이 5라면 5에서 멈춘다.
    # 초록이 된 것을 확인하고 다음 초에 이동하는 것
    position = P
    if T % (R+G) <= R:
        T += R - (T % (R+G))

    lights.pop(0)

T += L - position

print(T)
