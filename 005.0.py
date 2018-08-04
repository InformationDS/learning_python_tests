import random
secret = random.randint(1,10)
temp = input('猜猜心里的逼数:')
if temp.isdigit() == 0:
    print('傻子，你难道连整数都不知道是啥吗？')
    temp = input('重新输入吧：')
num = int(temp)
if num == secret:
    print('行行行，你是大佬你说了算')
else:
    if num > secret:
        print('你心里的逼数比这个小')
    else:
        print('你心里的逼数比这个大')
i = 1
while num != secret:
    temp = input('猜错了，请重新输入：')
    while temp.isdigit() == 0:
        print('傻子，你难道连整数都不知道是啥吗？')
        temp = input('重新输入吧：')
    num = int(temp)
    if num == secret:
        print('行行行，你是大佬你说了算')
        break
    else:
        if num > secret:
            print('你心里的逼数比这个小')
        else:
            print('你心里的逼数比这个大')
    i = i + 1
    if i >= 3:
        print('你丫猜了三次都没猜出来')
        break    
print('Game over')
