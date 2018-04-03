import math
def quadratic(a,b,c):
    delta = b * b - 4 * a *c
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
    else:
        x1 = None
        x2 = None
    return x1,x2
print('请依次输入系数(输入三个0退出程序）：')
a = float(input())
b = float(input())
c = float(input())
while a != 0 and b != 0 and c != 0:
    answer = quadratic(a,b,c)
    if answer == (None,None):
        print('No answer')
    else:
        print('answer =',answer)
    print('请依次输入系数(输入三个0退出程序）：')
    a = float(input())
    b = float(input())
    c = float(input())