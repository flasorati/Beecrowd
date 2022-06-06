def tabuada(numero):
    i = 1
    while i <= 10:
        print(f'{numero} x {i} = {numero*i}')
        i += 1
    print(end='----------\n') 


n1 = int(input())
n2 = int(input())

if n1 > n2:
    print('Nenhuma tabuada no intervalo!')

else:
    for i in range(n1, n2+1):
        tabuada(i)

