def solution(price, money, count):
    remain = money - int((price * count*(count+1)/2))
    return remain if remain < 0 else 0

price, money, count, result = 3, 20, 4, 10