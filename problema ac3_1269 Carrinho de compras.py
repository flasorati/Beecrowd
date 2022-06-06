def adicionar(i):
    lista.append(i)

def remover(i):
    if i in lista:
        lista.remove(i)
    else:
        print('código', i ,'não encontrado')
           
def exibir(lista):
    if lista != []:
        lista.sort()
        for i in range(len(lista)-1):
            print(lista[i], end=' ')
        print(lista[-1])        
        

lista = input().split()
if lista != []:
    for i in range(len(lista)):
        lista[i] = int(lista[i])

comando = input().split()

while comando[0] != 'encerrar':
    if comando[0] == 'adicionar':
        comando[1] = int(comando[1])
        adicionar(comando[1])

    elif comando[0] == 'remover':
        comando[1] = int(comando[1])
        remover(comando[1])

    elif comando[0] == 'exibir':
        exibir(lista)
    comando = input().split()
    
else:
    exibir(lista)
