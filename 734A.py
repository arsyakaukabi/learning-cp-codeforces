n = int(input())
s = input()

if s.count('D') > s.count('A'):
    print('Danik')
elif s.count('D') < s.count('A'):
    print('Anton')
else:
    print('Friendship')
