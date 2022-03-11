def f(s, N):
    if N < 3:
        return False
    s.sort()
    for i in range(N - 2):
        if s[i] + s[i + 1] > s[i + 2]:
            return True


N = int(input())
*s, = map(int, input().split())
print("YES" if f(s, N) else "NO")
