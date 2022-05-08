def solution(n, arr1, arr2):
    for i in range(n):
        tmp1 = list(map(int, format(arr1[i], 'b')))
        tmp2 = list(map(int, format(arr2[i], 'b')))
        tmp1 = (n - len(tmp1)) * [0] + tmp1
        tmp2 = (n - len(tmp2)) * [0] + tmp2
        arr1[i] = tmp1
        arr2[i] = tmp2
    result = []
    for i in range(n):
        result.append([])
        for j in range(n):
            result[i].append(
                '#' if arr1[i][j] or arr2[i][j] else ' '
            )
        result[i] = ''.join(result[i])
    return result


n1 = 5
arr1_1 = [9, 20, 28, 18, 11]
arr1_2 = [30, 1, 21, 17, 28]
n2 = 6
arr2_1 = [46, 33, 33, 22, 31, 50]
arr2_2 = [27, 56, 19, 14, 14, 10]
solution(n1, arr1_1, arr1_2)
solution(n2, arr2_1, arr2_2)