n  = int(input(f'son :'))

son = float(input('son 1 :'))
    
min_son = son
max_son = son

for i in range(2,n+1) :
   son = float(input(f'son {i}:'))
    
   if son > max_son :
    max_son = son
   if son < min_son :
    min_son = son

avg = (max_son + min_son)/2

print(avg)
