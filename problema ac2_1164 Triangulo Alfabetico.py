N = int(input())
i = 1
A = 65
if (1 <= N <= 26):
    while i <= N:
       caracter = chr(A) * i
       print(caracter)
       i += 1
       A += 1


