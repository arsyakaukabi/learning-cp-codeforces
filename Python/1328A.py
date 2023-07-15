t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    if n % k != 0:
        print(abs(n - k*(n // k + 1)))
    else:
        print(0)
