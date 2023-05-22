aux = input("Digite um numero positivo: ")
n = int(aux)

while n < 0:
    aux = input("Erro! Digite um inteiro positivo: ")
    n = int(aux)

soma =  0;
i = 1
while i <= n:
    soma = soma + i 
    i = i + 1

    print("Valor da soma vale ", soma)