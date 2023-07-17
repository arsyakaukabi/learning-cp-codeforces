for i in range(int(input())):
    count = 0
    a = "codeforces"
    s = input()
    for j in range(len(a)):
        if s[j] != a[j]:
            count += 1
    print(count)
