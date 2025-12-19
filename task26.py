
count = 0
for i in range(1,8):
    age = int(input(f'age {i} :'))
    if age < 21 :
       count += 1
print(count)