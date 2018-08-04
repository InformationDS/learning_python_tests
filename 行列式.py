#输入行列式
a = input('first: ')
b = input('second: ')
c = input('third: ')

#计算结果
a[0] * b[1] * c[2] + a[1] * b[2] * c[0] + a[2] * b[0] * c[1]-a[2] * b[1] * c[0] - a[1] * b[0] * c[2] - a[0] * b[2] * c[1]
