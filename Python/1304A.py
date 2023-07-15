t = int(input())

for i in range(t):
    x, y, a, b = map(int, input().split())
    time = (y-x)/(a+b)
    if time.is_integer():
        print(int(time))
    else:
        print(-1)
