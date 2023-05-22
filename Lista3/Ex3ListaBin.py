binario = int(input("Informe o número binário: "))

soma = 0 
pot = 1

while binario > 0:
    digito = binario % 10
    soma = soma + digito * pot
    binario = binario // 10
    pot = pot * 2

print(soma)