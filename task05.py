i = int(input('i :'))
n = int(input('n :'))

if n > 0 :
    for a in range(i,n+1):
        print(a)
else :
    for a in range(i,n-1,-1):
        print(a)