A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)

Atriangulo = (A*C)/2

pi = 3.14159
Acirculo = pi * C**2

Atrapezio = ((A+B)*C)/2

Aquadrado = B**2

Aretangulo = A * B

print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(Atriangulo, Acirculo, Atrapezio, Aquadrado, Aretangulo))


