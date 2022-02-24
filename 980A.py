s = input()
print('YES' if s.count('-') % (s.count('o') or 1) == 0 else 'NO')
