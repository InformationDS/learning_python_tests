for i in range(100,1000):
    sum = 0
    _i = i
    while _i:
        sum += (_i % 10) ** 3
        _i //= 10
    if i == sum:
        print(i)
