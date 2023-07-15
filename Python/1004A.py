n, d = map(int, input().split())
x = list(map(int, input().split()))
cities = 2

for i in range(n-1):
    if x[i+1]-x[i] >= 2*d:
        cities += 2 if x[i+1]-x[i] > 2*d else 1

print(cities)
