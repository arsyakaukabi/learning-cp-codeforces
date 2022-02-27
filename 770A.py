n, k = map(int, input().split())
s = 'abcdefghijklmnopqrstuvwxyz'
print(s[:k]*(n//k)+s[:n % k])
