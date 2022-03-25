import sys
from queue import PriorityQueue
sys.stdin = open('input.txt', 'r')

arr = list(map(int,input()))
dp = [0 for _ in range(len(arr)+1)]
if arr[0]:
    arr = [0] + arr
    dp[0], dp[1] = 1, 1
    for i in range(2, len(arr)):
        if arr[i] > 0:
            dp[i] += dp[i-1]
        # 여기 조건이 틀렸었음: 17~19는 조건에 포함되지 않기 때문에. 바보냐..?
        # if 1 <= arr[i-1] <= 2 and 0 <= arr[i] <= 6:
        digit2 = arr[i - 1] * 10 + arr[i]
        if 10 <= digit2 <= 26:
            dp[i] += dp[i-2]
    print(dp[len(arr)-1] % 1000000)
else:
    print(0)
