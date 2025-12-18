total = 0

for i in range(1,5) :
    mahsulot = int(input(f'Mahsulot  {i} :' ))


    total += mahsulot

result = total - (total * 0.10)

print(result)
