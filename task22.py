narx = float(input('narx 1 :'))

max_narx = narx
min_narx = narx 

for i in range(2,5+1):
    narx = float(input(f'narx {i} :'))
    if narx > max_narx:
        max_narx = narx
    if narx < narx :
        min_narx = narx 

avg = (max_narx + min_narx)/2

print(avg)