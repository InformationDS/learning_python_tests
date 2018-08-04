import random
secret = random.randint(1,10)
num = int(input('猜猜心里的逼数:'))
if num == secret:
    print('行行行，你是大佬你说了算')
else:
    if num > secret:
        print('你心里的逼数比这个小')
    else:
        print('你心里的逼数比这个大')
i = 1
while num != secret:
    num = int(input('猜错了，请重新输入：'))
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

            
