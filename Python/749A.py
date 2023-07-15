n = int(input())

if n % 2 == 0:
    k = int(n/2)
    print(str(k), "\n" + "2 "*(k))
else:
    k = int((n-1)/2)
    print(str(k), "\n" + "2 "*(k-1)+"3")
