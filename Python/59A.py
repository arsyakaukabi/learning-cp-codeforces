s = input()
count = 0
for i in s:
    if i.islower():
        count += 1

print(s.lower() if count >= len(s)-count else s.upper())
