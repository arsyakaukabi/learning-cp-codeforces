n = int(input())
a = *map(int, input().split()),
ans = 1
for i in range(n):
    L = R = i
    x = y = a[i]
    while R < n and y >= a[R]:
        y = a[R]
        R += 1
    while L-1 >= 0 and a[L-1] <= x:
        L -= 1
        x = a[L]
    ans = max(ans, R-L)
print(ans)
