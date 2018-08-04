while 1:
    temp = input('请输入年份(输入tc退出)：')
    if temp == 'tc':
        break
    while temp.isdigit() == 0:
        print('你确定这是年份？')
        temp = input('请重新输入：')
    year = int(temp)
    if year % 400 == 0:
        print(year,end = '')
        print('是闰年')
    elif (year % 4 == 0) and (year % 100 != 0):
        print(year,end = '')
        print('是闰年')
    else:
        print(year,end = '')
        print('是平年')
print('感谢使用')
