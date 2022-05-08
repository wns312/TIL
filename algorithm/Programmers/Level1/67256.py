def solution(numbers, hand):
    phone = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [-1, 0, -1],
    ]
    left, right = [3, 0], [3, 2]
    result = []
    for i in range(len(numbers)):
        n = numbers[i]
        if n in [1, 4, 7]:
            result.append('L')
            for i in range(3):
                if phone[i][0] == n:
                    left = [i, 0]
                    break
        elif n in [3, 6, 9]:
            result.append('R')
            for i in range(3):
                if phone[i][2] == n:
                    right = [i, 2]
                    break
        else:
            # 우선 숫자의 좌표 먼저 찾기
            r1, c1 = 0, 1
            for i in range(4):
                if phone[i][1] == n:
                    r1 = i
                    break
            l_dis = abs(left[0]-r1) + abs(left[1]-c1)
            r_dis = abs(right[0]-r1) + abs(right[1]-c1)
            if l_dis > r_dis:
                right = [r1, c1]
                result.append('R')
            elif l_dis < r_dis:
                left = [r1, c1]
                result.append('L')
            else:
                if hand == 'left':
                    left = [r1, c1]
                    result.append('L')
                else:
                    right = [r1, c1]
                    result.append('R')

    return ''.join(result)

