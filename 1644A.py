for _ in range(int(input())):
    s = input()
    count = 0
    for x in 'RGB':
        if x.lower() in s[:s.index(x)]:
            count += 1
    print('YNEOS'[count!=3::2])