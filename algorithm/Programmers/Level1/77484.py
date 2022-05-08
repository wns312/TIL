def solution(lottos, win_nums):
    lottos_len = len(lottos)
    correct_count, zero_count = 0, 0
    for i in range(lottos_len):
        if not lottos[i]:
            zero_count += 1
            continue
        if lottos[i] in win_nums:
            correct_count += 1
    return [
        6-(correct_count+zero_count)+1 if 6-(correct_count+zero_count)+1 <= 6 else 6,
        7-correct_count if 7-correct_count <= 6 else 6
    ]
