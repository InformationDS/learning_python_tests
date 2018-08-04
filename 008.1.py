x,y,z = 6,5,4
print(x if x < ( y if y < z else z) else ( y if y < z else z))

'''
    x, y, z = 6, 5, 4
    if x < y:
        small = x
        if z < small:
            small = z
    elif y < z:
        small = y
    else:
        small = z
'''
