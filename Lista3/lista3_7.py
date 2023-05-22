import math

numero = float(input("Digite um número: "))

if numero >= 0:
    raiz = math.sqrt(numero)
    print("A raiz quadrada de {} é {}".format(numero, raiz))

else:
    print("Impossível extrair raiz quadrada de {}".format(numero))