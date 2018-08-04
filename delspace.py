# -*- coding: utf-8 -*-
def trim(s):
    if len(s)>0:
        a = 0
        if s[a] == ' ':
            a = a+1
        b = len(s)-1
        if s[b] == ' ' and b >= a:
            b = b-1
        return s[a:b+1]