import sys
sys.stdin = open('input.txt', 'r')

# next_permutation 방식
N = int(input())
arr = list(map(int, input().split()))

is_exist = False
# 1. 뒤에서 부터 반복을 돌면서 만약 앞의 수가 뒤의 수보다 작다면
# 앞의 수를 x, 뒤의 수를 y라고 하고 경계를 나눈다
for i in range(N-1, 0, -1):
    if arr[i-1] < arr[i]:
        x, y = i-1, i
        # 2. 뒷부분만 뒤에서 앞으로 반복을 돌면서 x보다 큰 수가 있다면 둘을 swap한다
        for j in range(N-1, x, -1):
            if arr[x] < arr[j]:
                arr[x], arr[j] = arr[j], arr[x]
                # 3. 뒷 부분을 오름차순 정렬해준 새 배열을 만든다
                arr = arr[:y] + sorted(arr[y:])
                is_exist = True
                break
        break

if is_exist:
    print(' '.join(map(str, arr)))
else:
    print(-1)









# # 나름대로 푼 문제. 하지만 next_permutation 알고리즘이 있다.
#
# sys.setrecursionlimit(10003)
# # 맞긴 맞았는데... 이걸 맞았다고 해야하나??
# # 맞았지만 수정해야 하는 부분
# # 1. 재귀의 깊이를 수정하지 않고도 풀기 (while문?)
# # 전체를 돌리면 시간 초과가 뜬다 -> 백트래킹 필요
# # 모든배열을 구하면 안되고, 직접 구현으로 풀어야 함 -> 메모리 초과
# N = int(input())
# ex = [i for i in range(1, N+1)]
# cur_order = list(map(int, input().split()))
# visit = [False] * N
# # 시작순열 : root_arr
# # 찾아야 할 순열 : arr_to_find
# # 출력해야할 순열 : arr_to_print
# # 방문처리 배열 : visited
# # 깊이 : idx
# # is_find : 원래 순열을 찾았는지
# # is_print : 출력해야할 순열을 출력했는지
#
# def perm(root_arr, arr_to_find, arr_to_print, visited, idx, is_find, is_print):
#
#
#     # break point를 넣어준다
#     if idx == len(arr_to_find):
#         if arr_to_print == arr_to_find:
#             return True, False
#         if is_find and not is_print:
#             [print(el, end=' ') for el in arr_to_print]
#             return True, True
#         return False, False
#     # 계산 로직
#     for i in range(len(arr_to_find)):
#         if not visited[i]:
#             visited[i] = True
#             arr_to_print.append(root_arr[i])
#             if not is_find and arr_to_find[idx] > arr_to_print[idx]:
#                 pass
#             else:
#                 is_find, is_print = perm(root_arr, arr_to_find, arr_to_print, visited, idx+1, is_find, is_print)
#             if is_find and is_print:
#                 break
#             visited[i] = False
#             arr_to_print.pop(-1)
#     return is_find, is_print
#
#
# had_find, had_visit = perm(ex, cur_order, [], visit, 0, False, False)
# if not had_find or not had_visit:
#     print(-1)