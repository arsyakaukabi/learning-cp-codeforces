I = lambda:map(int,input().split())
n,b,d=I();*a,=I()
c=0;ans=0
for i in range(n):
    if a[i] <= b:
        c+=a[i]
    if c > d:
        ans += 1
        c = 0
print(ans)
