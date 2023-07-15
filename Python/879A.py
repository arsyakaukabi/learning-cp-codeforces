n = int(input())
ans = 0
for i in range(n):
    s, d = map(int, input().split())
    if s > ans:
        ans = s
    else:
        ans = s + d*((ans-s)//d+1)
print(ans)
