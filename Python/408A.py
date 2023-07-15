n = int(input())
k = map(int, input().split())
sec = []

for i in range(n):
    m = list(map(int, input().split()))
    sec.append(sum(m)*5+len(m)*15)

print(min(sec))
