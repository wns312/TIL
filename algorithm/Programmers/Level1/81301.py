def solution(s: str):
    nums = [
        'zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine'
    ]
    for i in range(len(nums)):
        s = s.replace(nums[i], str(i))
    return int(s)
