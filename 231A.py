n = int(input())
count = 0

for i in range(n):
    n_line = [int(item) for item in input().split()]
    if sum(n_line) >= 2:
        count += 1

print(count)
