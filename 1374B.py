t = int(input())

for i in range(t):
    count = 0
    n = int(input())
    while n > 1:
        if n % 6 == 0:
            n /= 6; count += 1
        elif n % 2 != 0:
            n *= 2; count += 1
        else:
            n = 0; count = -1
    print(count)
