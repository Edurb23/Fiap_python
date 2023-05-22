#Decidir o vencedor de uma partida de futebol
#os times São Paulo e Barcelona

#int(input) jução de int com imput

#elif => else + if



golA = int(input("Gols do Real Madrid: "))
golB = int(input("Gols do Barcelona "))


if golA == golB:
    print("Empate")
    #decisão por pênaltis
else:
    if golA > golB:
        print("O Real Madrid venceu o Barcelona")
    else:
        print("O Barcelona venceu o Real Madrid")

        

print("Fim do programa")