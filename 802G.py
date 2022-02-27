a = 'heidi'
c = 0
for i in input():
    if i == a[c]:
        c += 1
        if c == 5:
            print('YES')
            quit()
print('NO')
