k, n, w = map(int, input().split())
b = w*(w+1)/2
b = int(b*k-n)
print(b if b >= 0 else 0)
