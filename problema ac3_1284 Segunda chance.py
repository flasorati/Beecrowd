def cria_lista(qtd_alunos):
    notas1 = []
    for i in range(qtd_alunos):
        nota = float(input())
        notas1.append(nota)
    return notas1
        
    notas2 = []
    for i in range(qtd_alunos):
        nota = float(input())
        notas2.append(nota)
    alunos.append(notas2)
    return notas2

def conta_alteradas(notas1, notas2):
    notas = len(notas1)
    cont = 0
    for i in range(notas):
        if notas2[i] == 10:
            if notas1[i] < 10:
                cont += 1     
    print('NOTAS ALTERADAS:', cont)

def imprime_notas(notas1, notas2):
    notas = len(notas1)
    for i in range(notas):
        if notas2[i] == 10:
            if notas1[i] <= 8:
                notas2[i] = notas1[i] + 2
                print(f'*({i+1:03}) original: {notas1[i]:0>5.2f} | final: {notas2[i]:0>5.2f}') 
            elif notas1[i] == 9:
                notas2[i] = 10
                print(f'*({i+1:03}) original: {notas1[i]:0>5.2f} | final: {notas2[i]:0>5.2f}')
            else:
                notas2[i] = 10
                print(f'-({i+1:03}) original: {notas1[i]:0>5.2f} | final: {notas2[i]:0>5.2f}')
        else:
            print(f'-({i+1:03}) original: {notas1[i]:0>5.2f} | final: {notas1[i]:0>5.2f}')

qtd_alunos = int(input())
notas1 = cria_lista(qtd_alunos)
notas2 = cria_lista(qtd_alunos)
conta_alteradas(notas1, notas2)
imprime_notas(notas1, notas2)

