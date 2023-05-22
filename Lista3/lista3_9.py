numA = float(input("Digite um número: "))
op = input("Operador: ")
numB = float(input("Digite um número: "))

fez_conta = True

if op == '+':
    resultado = numA + numB
elif op == '-':
    resultado = numA - numB
elif op == '*':
    resultado = numA * numB
elif op == '/':
    if numB != 0:
        resultado = numA / numB
    else:
        fez_conta = False
        print("Impossível dividir por zero!")
else:
    fez_conta = False
    print("Operador inválido!")    

if fez_conta:
    print("Resultado", resultado)