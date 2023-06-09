a = 4
maxx = 0

def f(x, h):
    if x >= maxx and (h == a or h == 2):
        return True
    if h < a and x >= maxx:
        return False
    if h == a and x < maxx:
        return False
    else:
        if h % 2:
            return f(x + 1, h + 1) or f(x * 2, h + 1)
        return f(x + 1, h + 1) or f(x * 2, h + 1)

def g(x, h):
    if x >= maxx and h == 2:
        return True
    if h < a and x >= maxx:
        return False
    if h == a and x < maxx:
        return False
    else:
        if h % 2:
            return f(x + 1, h + 1) or f(x * 2, h + 1)
        return f(x + 1, h + 1) and f(x * 2, h + 1)

for i in range(maxx):
    if f(i, 0): #and g(i, 0):
        print(i)