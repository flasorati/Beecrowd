total = 0
doacao = float(input())

while doacao != -1:
    total += doacao
    doacao = float(input())


print(f'VC$ {total:.2f}')
print(f'R$ {total*2.5:.2f}')



