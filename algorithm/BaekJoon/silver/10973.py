import sys
sys.stdin = open('input.txt', 'r')

# prev_permutation

N = int(input())
arr = list(map(int, input().split()))
is_exist = False
# 1. 뒤에서 앞으로 반복을 돈다
for i in range(N-1, 0, -1):
    # 2. 앞의 수가 뒤의 수보다 큰경우
    if arr[i-1] > arr[i]:
        # 앞의 수를 x, 뒤의 수를 y로 하고 둘을 경계로 한다
        x, y = i-1, i

        # 3. 다시 뒤에서 앞으로 뒷부분을 기준으로 반복을 돌린다
        for j in range(N-1, y-1, -1):
            # 4. 만약 x의 앞이 현재 인덱스 값보다 크다면 둘을 swap 한다
            if arr[x] > arr[j]:
                arr[x], arr[j] = arr[j], arr[x]
                # 5. swap 한 뒤, 뒤의 배열을 내림차순 정렬 해준다.
                arr = arr[:y] + list(reversed(arr[y:]))
                # 이전 순열의 존재여부를 체크 후 break
                is_exist = True
                break

        # if절에 들어왔다는 것 자체가 이전 순열이 있다는 의미이므로 break을 한다
        break

if is_exist:
    print(' '.join(map(str, arr)))
else:
    print(-1)
