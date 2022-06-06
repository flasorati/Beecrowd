nome = input()
salario_fixo = float(input())
valor_vendas = float(input())

total_salario = salario_fixo + (valor_vendas * 15/100)

print("TOTAL = R$ {:.2f}".format(total_salario))

