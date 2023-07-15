from sys import stdin
from collections import Counter
for _ in range(int(input())):
    input();f=1
    *s, = stdin.readline().split()
    counts = Counter(s)
    k = set(s)
    for i in k:
        if counts[i]>=3:
            print(i);f=0;break
    if f:print(-1)
