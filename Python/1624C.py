for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    s = set()
    for i in a:
        while((i > n or i in s) and i > 1):
            i //= 2
        s.add(i)
    print('YES' if len(s) == n else 'NO')

