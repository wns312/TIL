def solution(numbers):
    numbers.sort()
    result = 0
    # 첫 숫자 처리
    if numbers[0] != 0:
        for i in range(1, numbers[0]):
            result += i
    # 마지막 숫자 처리
    if numbers[-1] != 9:
        for i in range(numbers[-1]+1, 10):
            result += i

    # 중간 숫자 처리
    for i in range(1, len(numbers)):
        for j in range(numbers[i-1]+1, numbers[i]):
            result += j

    return result
