while 1:
    temp = input('请输入一个整数（输入Q结束程序）：')
    if temp == 'Q':
        break
    if temp.isdigit():
        num = int(temp)
        print('十进制 -> 十六进制：%d -> %#x'%(num,num))
        print('十进制 -> 八进制：%d -> %#o'%(num,num))
        print('十进制 -> 二进制：%d -> ',end = '')
        print(bin(num))
    else:
        print('您输入的不是整数！')
    
