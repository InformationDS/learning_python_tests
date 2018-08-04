secret = '0914zh0805gg'
sec = input('请输入密码：')
x = 3
while 1:
    if '*' in sec:
        print('密码中不能含有“*”号！您还有'+ str(x) +'次机会！',end = '')
        sec = input('请输入密码：')
        continue
    if sec != '0914zh0805gg':
        x -= 1
        if sec == '喜欢一个人喜欢了七年':
            print('密码错误，但是你懂我，你还有'+ str(x) +'次机会！')
            sec = input('请输入密码：')
        else:
            print('密码错误，你还有'+ str(x) +'次机会！')
            sec = input('请输入密码：')
    else:
        print('密码正确，正在进入程序...')
        break
        

            
