start = int(input('start :'))
step = int(input('step :'))

if start <= 15 :
    for i in range(start,15+1,step) :
        print(i)
else :
     for i in range(start,15-1,-step) :
        print(i)