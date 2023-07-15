i = lambda: map(int, input().split())
n, k = i()
a = list(i())
print(sum(v >= max(1, a[k-1]) for v in a))
