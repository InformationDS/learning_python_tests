while 1:
    temp = input('请输入成绩（输入tc退出）：')
    if temp == 'tc':
        break
    while not temp.isdigit():
        temp = input('请确定输入的是整数：')
    grade = int(temp)
    if 90 <= grade < 100:
        print('A')
    elif 80 <= grade < 90:
        print('B')
    elif 60 <= grade < 80:
        print('C')
    elif 0 <= grade <60: 
        print('D')
    else:
        print('请输入正确的分数')
