s = input()
cyc = set()
for i in range(len(s)):
    cyc.add(s[i:]+s[:i])

print(len(cyc))
