import sys
sys.stdin = open('input.txt', 'r')
# 트럭대수, 다리길이, 최대하중
N, W, L = map(int, input().split())
# 각 트럭의 무게
trucks = list(map(int, input().split()))

bridge = [0] * W
bridge_sum = 0
time = 0
while trucks or bridge_sum:
    time += 1
    print(f'{time}초')
    print(f'전 다리 {bridge}')
    bridge_sum -= bridge.pop(0)
    if trucks and bridge_sum + trucks[0] <= L:
        bridge.append(trucks.pop(0))
        bridge_sum += bridge[-1]
    else:
        bridge.append(0)
    print(f'후 다리 {bridge}')
    print()
print(time)