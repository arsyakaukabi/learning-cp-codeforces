for _ in range(int(input())):
    s,c=input(),0
    for i in s:
        if i=='A':c+=1
        else:c-=1
        if c<0:break
    print('NYOE S'[(c>=0)&(s[-1]=='B')::2])
