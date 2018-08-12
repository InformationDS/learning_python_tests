member = ['小甲鱼','黑夜','迷途','怡静','秋舞斜阳']
member.insert(1,88)
member.insert(3,90)
member.insert(5,85)
member.insert(7,90)
member.append(88)
#方法二
x = 0
length = len(member)
while x < length:
    print(member[x],member[x+1])
    x += 2
