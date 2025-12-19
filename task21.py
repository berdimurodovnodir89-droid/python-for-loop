a1 = 0
n = int(input('son :'))

for i in range(1, n + 1) :
    if i % 2 == 0 :
        a1 += i

a2 = 0
for i in range(1, n + 1) :
    if i % 2 != 0 :
        a2 += i


print(f'juft son {a1} toq son {a2}')