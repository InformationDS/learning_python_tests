from functools import reduce
def prod(L):
    def sum(x, y):
        return x * y

    return reduce(sum, L)
#测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')