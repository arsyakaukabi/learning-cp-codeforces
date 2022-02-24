shifting = input()
a = "qwertyuiopasdfghjkl;zxcvbnm,./"

for word in input():
    print(a[a.index(word)+(1 if shifting == 'L' else -1)], end='')
