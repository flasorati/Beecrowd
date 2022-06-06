def recebe_tempo():
    lista = []
    while True:
        tempo = int(input())
        if tempo < 0:
            break
        lista.append(tempo)
    return lista

def calcula_media(lista_tempo):
    media = sum(lista_tempo)/len(lista_tempo)
    print(f'MEDIA: {media:.2f}')
    return media

def imprime_lista(lista_tempo, media_tempo):
    for tempo in lista_tempo:
        if tempo < media_tempo:
            print(tempo)       

lista_tempo = recebe_tempo()
media_tempo = calcula_media(lista_tempo)
imprime_lista(lista_tempo, media_tempo)

def preenche_tabela(qtd_canais):
    tabela = []
    for i in range(qtd_canais):
        canal = input().split(';')
        canal[1] = int(canal[1])
        canal[2] = float(canal[2])
        canal[3] = (canal[3] == 'sim')
        tabela.append(canal)
    return tabela        
            
     
 
qtd_canais = int(input())


tabela = preenche_tabela(qtd_canais)
bonus_premium = float(input())
bonus_basico = float(input())

print(end='-----\n')
print('BÔNUS')
print(end='-----\n')
calcula_bonus(tabela, bonus_premium, bonus_basico)
