n = int(input())
*v, = map(int, input().split())
u = sorted(v)
for i in range(1, n):
    v[i] += v[i-1]
    u[i] += u[i-1]
for _ in range(int(input())):
    t, l, r = map(int, input().split())
    if t == 2:
        print(u[r-1]-u[l-2] if l-1 != 0 else u[r-1])
    else:
        print(v[r-1]-v[l-2] if l-1 != 0 else v[r-1])
