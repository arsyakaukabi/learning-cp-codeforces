n = int(input())
a = b = 0
passenger_now = []

for i in range(n):
    new_a, new_b = map(int, input().split())
    a += new_a
    b += new_b
    passenger_now.append(b - a)

print(max(passenger_now))
