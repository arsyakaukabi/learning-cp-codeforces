n = int(input())
*h, = map(int, input().split())
e = 0
c = h[0]
for i in range(n-1):
    p = h[i]-h[i+1]
    if p + e < 0:
        c += abs(p+e)
        e = 0
    else:
        e += p
    print(c, e)
