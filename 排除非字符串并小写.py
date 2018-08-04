# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = []
for x in L1:
    if isinstance(x,str):
        L2.append(x)
L2 = [x.lower() for x in L2]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')