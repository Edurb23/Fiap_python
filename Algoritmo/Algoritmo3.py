valor = input("Digite número: ")
numA = float(valor)
op = input("Operador (+-*/): ")
valor = input ("Digite número: ")
numB = float(valor)

if op == '+':
    result = numA + numB

elif op == '-':
    result = numA - numB

elif op == '*':
    result = numA * numB

elif op == '/':
    result = numA / numB

print("Resultado é:", result)        
