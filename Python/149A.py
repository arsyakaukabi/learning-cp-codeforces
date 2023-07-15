k = int(input())
a_i = list(map(int, input().strip().split()))
a_i.sort(reverse=True)
sum = i = 0

while sum < k and i != len(a_i):
    sum += a_i[i]
    i += 1

if i == len(a_i) and sum != k:
    print(-1)
else:
    print(i)
