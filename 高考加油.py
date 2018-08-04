#仙中高考加油

sentence = input('Sentence: ')

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width)//2

print()
print(' ' *left_margin + '+' + '-' *(box_width+4) + '+')
print(' '* left_margin + '|' + ' ' * (text_width+10)   + '|')
print(' ' *left_margin + '|' + ' ' * 2 + sentence + ' ' * 2 + '|')
print(' '* left_margin + '|' + ' ' * (text_width+10) + '|')
print(' ' *left_margin + '+' + '-' *(box_width+4) + '+')
print()

from turtle import *
def curvemove():
    for i in range(200):
        right(1)
        forward(1)
color('red','pink')
begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()
done()


