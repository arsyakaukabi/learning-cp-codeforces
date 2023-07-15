import math

n, h = map(int, input().split())
a_i = list(map(int, input().split()))
road = 0

for i in a_i:
    road += math.ceil(i/h)

print(road)
