print('red\tyellow\tgreen\t')
for r in range(0,4):
    for y in range(0,4):
        for g in range(2,7):
            if r + y + g == 8:
                print(r, '\t', y, '\t', g, '\t')
