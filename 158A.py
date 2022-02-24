i = lambda: map(int, input().split())
n, k = i()
l = list(i())
print(sum(v >= max(1, l[k-1]) for v in l))
