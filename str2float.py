from functools import reduce

def str2float(s):
    dights = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def _2dight(s):
        return dights[s]

    def fn(x, y):
        return 10 * x + y

    count = s.find('.')
    n = len(s[:count])
    return reduce(fn, map(_2dight, s[0:count])) + reduce(fn, map(_2dight, s[count + 1:])) / pow(10, n)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')