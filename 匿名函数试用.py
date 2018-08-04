# -*- coding: utf-8 -*-
#原版
#def is_odd(n):
#    return n % 2 == 1

#L = list(filter(is_odd, range(1, 20)))
#print(L)

#匿名函数修改版
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)