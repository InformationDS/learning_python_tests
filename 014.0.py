# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

secret = input('请输入需要检查的密码组合：')
length = len(secret)

while secret.isspace():
    secret = input('您输入的密码为空，请重新输入：')
    length = len(secret)
level = 0

#判断密码长度
if 8 <= length < 16:
    level +=1
elif length >= 16:
    level += 2

#判断密码中的数字、字母及特殊字符
for i in secret:
    if i in symbols:
        level += 1
        break

for i in secret:
    if i in chars:
        level += 1
        break

for i in secret:
    if i in nums:
        level += 1
        break
        
#判断开头字符
if secret[0] in chars:
    level += 1

#判断级别并输出
print('您的密码级别为：',end = '')
if level < 3 or length < 8:
    print('低')
elif level < 6:
    print('中')
else:
    print('高')
if level < 6:
    print('请按以下方式提升您的密码安全级别：\n\
    \t1.密码必须由数组、字母及特殊字符三种组合\n\
    \t2.密码只能由字母开头\n\
    \t3.密码长度不能低于16位')
else:
    print('请继续保持')
