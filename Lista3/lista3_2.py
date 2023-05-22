numA = int(input("INSIRA UM NUMERO: "))
numB = int(input("INSIRA UM NUMERO: "))


if numA == numB:
    print("Empate")
    #decisão por pênaltis
else:
    if numA > numB:
        print("O NUMERO A E MAIOR QUE O NUMERO B")
    else:
        print("O NUMERO B E MAIOR QUE O NUMERO A")

        

print("Fim do programa")