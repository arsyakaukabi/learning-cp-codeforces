def infinity():
    i = 2
    while True:
        yield i
        i += 1


t = int(input())

for i in range(t):
    n = int(input())
    for k in infinity():
        x = n/(2**k-1)
        if x.is_integer():
            break
    print(int(x))
