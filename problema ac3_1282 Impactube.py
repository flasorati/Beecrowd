def calcula_bonus(tabela, bonus_premium, bonus_basico):
    for canal in tabela:
        if canal[3] == True:
            bonusP = canal[2] + (canal[1]//1000) * bonus_premium
            print(f'{canal[0]}: R$ {bonusP:.2f}')
        else:
            bonusB = canal[2] + (canal[1]//1000) * bonus_basico
            print(f'{canal[0]}: R$ {bonusB:.2f}')
         

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
