import sys
sys.stdin = open('input.txt', 'r')

# I V X L 만을 사용한다
# 각각 1, 5, 10, 50 을 의미한다
# 각 문자가 의미하는 수는 각 문자가 의미하는 수를 모두 합친 값이다
# 실제 로마 숫자와 달리 순서를 신경쓰지 않는다 (IX는 원래 9이지만, 여기서는 11이다)

# 로마 숫자를 N개 사용해서 만들 수 있는 서로 다른 수의 개수를 구하자
N = int(input())
numbers = [1, 5, 10, 50]
r = set(numbers)
for i in range(N-1):
    new_r = set()
    for n in r:
        for j in range(4):
            new_r.add(n+numbers[j])
    r = new_r
print(len(r))



# combinations_with_replacement는 모든 조합을 구해주는 도구로
# 첫번째 인수에 반복 가능한 iter를 넣고, 뒤에 길이가 몇인 것을 뽑을지 지정한다
# from itertools import combinations_with_replacement
# N = int(input())
#
# result = {
#     sum(comb)
#     for comb in combinations_with_replacement([1, 5, 10, 50], N)
# }
#
# print(len(result))



