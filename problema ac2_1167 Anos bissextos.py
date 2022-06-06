Ainicio = int(input())
Afim = int(input())

anos = list(range(Ainicio, Afim))
anos.append(Afim)

i = 0
contbissexto = 0
if 0 <= Ainicio <= Afim <= 9999:
    for i in anos:
        if (i % 4 == 0 and not i % 100 == 0) or i % 400 == 0: 
            print(i)
            contbissexto += 1
            i += 1

    print("bissextos:", contbissexto)





