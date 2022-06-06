Ninicio = int(input())
Nfim = int(input())

contPrimos = 0
for i in range(Ninicio, Nfim + 1):
    if i > 1:
        for x in range(2, i):
            if i % x == 0:
                break
        else:
            print(i)
            contPrimos += 1
print('primos:',contPrimos)



