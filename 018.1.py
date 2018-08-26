def flower(temp,isFind):
    sum = 0
    for i in range(3):
        sum += int(temp[i]) ** 3
    if sum == int(temp):
        isFind = 1
    return isFind

temp = input('请输入一个三位数：')
isFind = 0

while temp.isdigit() == 0 or len(temp) != 3:
    temp = input('您输入的不是一个三位数，请重新输入：')


if flower(temp,isFind):
    print(temp + '是一个水仙花数')
else:
    print(temp + '不是一个水仙花数')
    


