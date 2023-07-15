t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    m1 = (2*b-c)/a  # [ma,b,c]
    m2 = (c+a)/(2*b)  # [a,mb,c]
    m3 = (2*b-a)/c  # [a,b,mc]

    if m1.is_integer() and m1 > 0 or \
        m2.is_integer() and m2 > 0 or \
            m3.is_integer() and m3 > 0:
        print("YES")
    else:
        print("NO")
