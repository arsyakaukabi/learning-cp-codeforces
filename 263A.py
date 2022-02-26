for i in range(5):
    a = list(map(int, input().split()))
    if 1 in a:
        count = abs(a.index(1)-2)
        count += abs(2-i)
print(count)
