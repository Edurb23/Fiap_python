notA = float(input('Informe uma nota de 0 a 10: '))

while notaA < 0 or notaA > 10:
    print("Nota invalida, digite novamente: ")
    notA = float(input("Informen a nota: "))

notaB = float(input("Informe outra nota de 0 a 10: "))
while notaB < 0 or notaB > 10:
    print("Nota invalida, digite novamente: ")
    notB = float(input("Informen a nota: "))

media = (notA + notaB) / 2

print("A media vale", media)