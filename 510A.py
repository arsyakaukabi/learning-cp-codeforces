n, m = map(int, input().split())

for i in range(1, n+1):
    if i % 4 == 0:
        print("#"+"."*(m-1))
    elif i % 2 == 0:
        print("."*(m-1)+"#")
    else:
        print("#" * m)
