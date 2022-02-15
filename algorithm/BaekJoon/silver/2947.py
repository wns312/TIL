import sys
sys.stdin = open('input.txt', 'r')

arr = list(map(int, input().split()))
while True:
    for i in range(1, 5):
        if arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            print(" ".join(map(str, arr)))
    if arr[0] < arr[1] < arr[2] < arr[3] < arr[4]:
        break


# 첫 번째 조각의 수가 두 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 두 번째 조각의 수가 세 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 세 번째 조각의 수가 네 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 네 번째 조각의 수가 다섯 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 만약 순서가 1, 2, 3, 4, 5 순서가 아니라면 1 단계로 다시 간다.
