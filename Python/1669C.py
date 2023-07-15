def getParity( n ):
    if n % 2 == 0:return 1
    else:return 0

for _ in range(int(input())):
    input()
    *a, = map(int, input().split())
    flag=[]
    for i in a[0::2]:
        flag+=[getParity(i)]
    if len(set(flag)) > 1:
        print('NO')
    else:
        flag=[]
        for i in a[1::2]:
            flag+=[getParity(i)]
        if len(set(flag)) > 1:
            print('NO')
        else:
            print('YES')