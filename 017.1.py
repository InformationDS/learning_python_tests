def gcd(x,y):
    while y:
        r = x % y
        x = y
        y = r

    return x
        
        
        
