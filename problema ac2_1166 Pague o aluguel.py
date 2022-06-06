total = 0
vdivida = int(input())
vparcela = int(input())

i = 1
while vdivida > vparcela:
    vdepois = vdivida - vparcela
    print('pagamento:', i)
    print('antes =',vdivida)
    print('depois =',vdepois, end='\n-----\n')
    vdivida = vdepois
    i += 1
if vdivida <= vparcela:
    resto = 0
    print('pagamento:', i)
    print('antes =',vdivida)
    print('depois =',resto, end='\n-----\n')




