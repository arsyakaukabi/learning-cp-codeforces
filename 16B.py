n, m = map(int, input().split())
v = 0
a = sorted((list(map(int, input().split()))[::-1] for i in range(m)), reverse=True)
i = 0
while n > 0 and m > 0:
    x = min(a[i][1], n)
    v += a[i][0] * x
    n -= x
    m -= 1
    i += 1
print(v)
