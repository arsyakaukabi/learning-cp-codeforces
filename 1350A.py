t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    for j in range(2, n+1):
        if n % j == 0:
            print(n+j+(k-1)*2)
            break
