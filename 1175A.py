t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    step = 0
    while n != 0:
        step += n % k + 1
        n //= k
    print(step-1)
