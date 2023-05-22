n = float(input("Informe um número: "))

raiz = 0.000001
incremento = 0.000001

while raiz * raiz < n:
    raiz = raiz + incremento

print("Raiz aproximada ", raiz)
print("Raiz exata", n ** 0.5)