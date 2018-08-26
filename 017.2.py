def dec2bin(dec):
    temp = []
    result = ''

    while dec:
        quo = dec % 2
        dec = dec // 2
        temp.qppend(quo)

    while temp:
        result += temp.pop()

    return result
