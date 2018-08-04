i = 7
x = 1
while 1:
    if (i % 2 == 1) and (i % 3 == 2) and (i % 5 == 4) and (i % 6 == 5):
        print('有'+ str(i) + '级台阶')
        break
    else:
        i = 7 * (x + 1)
    x += 1 
