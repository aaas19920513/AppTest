

def t():
    for a in range(1,4):
        yield a

a = t()
for item in a:
    b = item +1
    print b
