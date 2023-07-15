n = int(input())
length = 0

for i in range(n):
    xi, yi = map(int, input().split())
    length = max(length, xi+yi)

print(length)
