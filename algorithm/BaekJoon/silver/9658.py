import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
print('CY' if N % 7 == 1 or N % 7 == 3 else 'SK')

# DP로 풀었을 때는 왜 틀린거지..? 로직은 같은데
