n = int(input())
teskari = 0

for digit in str(n)[::-1]:
    teskari = teskari * 10 + int(digit)

print(teskari)