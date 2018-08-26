def panduan(sentence):
    i = 1
    length = len(sentence)
    last = length - 1
    length //= 2
    for each in range(length):
        if sentence[each] != sentence[last]:
            i = 0
        last -= 1

    return i
        
temp = input('请输入一句话：')
if panduan(temp):
    print('是回文联！')
else:
    print('不是回文联！')
