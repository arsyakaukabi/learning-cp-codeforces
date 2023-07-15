n, a = map(int, input().split())
t = *map(int, input().split()),
x = sum(t)
for i in range(min(a-1, n-a)):
    if t[i+a] + t[a-2-i] == 1:
        x -= 1
print(x)
