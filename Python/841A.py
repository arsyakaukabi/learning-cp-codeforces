n, k = map(int, input().split())
s = input()
count = 0

for i in set(s):
    if s.count(i) > k:
        count += 1

print("NO" if count > 0 else "YES")
