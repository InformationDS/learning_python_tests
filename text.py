# -*- coding: utf-8 -*-
import time, functools

def metric(func):
    @functools.wraps(func)
    def f1(*args, **kv):
        start_time = time.time()
#        print("start time: %s"%(time.asctime(time.localtime(start_time))))
        tmp = func(*args, **kv)
        end_time = time.time()
        print("%s executed in %.0f ms"%(func.__name__, (end_time-start_time)*1000))
        return tmp
    return f1
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')