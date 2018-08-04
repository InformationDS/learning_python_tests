num = int(input('请输入一个整数：'))
while num:
    print(' '*(num - 1),end = '')
    print('*'*num)
    num -= 1
