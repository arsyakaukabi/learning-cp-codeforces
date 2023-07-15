b, k = map(int, input().split())
a = list(map(int, input().split()))
n = sum(a[:-1]*b, a[-1])
print('even' if n % 2 == 0 else 'odd')
