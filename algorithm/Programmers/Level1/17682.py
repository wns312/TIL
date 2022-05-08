def solution(dart_result):
    dart_result = list(dart_result)
    price = 1
    total_score = 0
    splited_result = []
    while dart_result:
        shot = dart_result.pop(-1)
        sign = 1
        if shot not in 'SDT' and shot in '*#':
            price = price*2 if shot in '*' else -1
            sign = -1 if shot == '#' else 2
            shot = dart_result.pop(-1)

        shot = dart_result.pop(-1) + shot
        if shot[0] == '0' and dart_result and dart_result[-1] not in 'SDT*#':
            shot = dart_result.pop(-1) + shot
        splited_result.append([shot, sign])
    splited_result = splited_result[::-1]
    for i in range(len(splited_result)-1):
        if splited_result[i+1][1] > 1:
            splited_result[i][1] *= splited_result[i+1][1]
    for i in range(len(splited_result)):
        shot = splited_result[i][0]
        shot, mul = int(shot[:-1]), shot[-1]
        if mul == 'S':
            mul = 1
        elif mul == 'D':
            mul = 2
        else:
            mul = 3
        total_score += shot ** mul * splited_result[i][1]

    return total_score


dart_result1, r1 = '1S2D*3T', 37
dart_result2, r2 = '1D2S#10S', 9
dart_result3, r3 = '1D2S0T', 3
dart_result4, r4 = '1S*2T*3S', 23
dart_result5, r5 = '1D#2S*3S', 5
dart_result6, r6 = '1T2D3D#', -4
dart_result7, r7 = '1D2S3T*', 59

