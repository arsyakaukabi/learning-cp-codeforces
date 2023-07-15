A = 0
B = 0
C = 0
for _ in range(3):
    s = input()
    if s == 'A<B' or s == 'B>A':
        B += 1
    elif s == 'A>B' or s == 'B<A':
        A += 1
    elif s == 'C<B' or s == 'B>C':
        B += 1
    elif s == 'C>B' or s == 'B<C':
        C += 1
    if s == 'A<C' or s == 'C>A':
        C += 1
    elif s == 'A>C' or s == 'C<A':
        A += 1
if A < B < C:
    print('ABC')
elif B < A < C:
    print('BAC')
elif C < A < B:
    print('CAB')
elif A < C < B:
    print('ACB')
elif B < C < A:
    print('BCA')
elif C < B < A:
    print('CBA')
else:
    print('Impossible')
