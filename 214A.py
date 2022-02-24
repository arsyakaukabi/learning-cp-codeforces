n, m = map(int, input().split())
ans = 0
for a in range(max(n, m)+1):
    b = n-a**2
    ans += b >= 0 and a+b**2 == m
print(ans)
